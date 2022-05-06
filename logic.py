from futoshiki import Futoshiki
import itertools as it


# Every cell has to contain at least a number
def rule_1(grid: Futoshiki):
	clauses = []
	for i in range(0, grid.side):
		for j in range(0, grid.side):
			clauses += [tuple(grid[i][j].booleans)]
	return clauses


# Every cell can't contain two numbers
def rule_2(grid: Futoshiki):
	clauses = []
	for i in range(0, grid.side):
		for j in range(0, grid.side):
			clauses += list(it.combinations(-grid[i][j].booleans, 2))
	return clauses


# Every cell has to respect pre-assigned values
def rule_3(grid: Futoshiki):
	clauses = []
	for i in range(0, grid.side):
		for j in range(0, grid.side):
			if grid[i][j].value != 0:
				clauses += [(grid[i][j][grid[i][j].value],)]
	return clauses


# Each line can't contain two times the same number
def rule_4(grid: Futoshiki):
	clauses = []
	for i in range(0, grid.side):
		for x in range(1, grid.side+1):
			clauses += [*list(it.combinations([-grid[i][j][x] for j in range(0, grid.side)], 2))]
	return clauses


# Each column can't contain two times the same number
def rule_5(grid: Futoshiki):
	clauses = []
	for j in range(0, grid.side):
		for x in range(1, grid.side+1):
			clauses += [*list(it.combinations([-grid[i][j][x] for i in range(0, grid.side)], 2))]
	return clauses


# Numbers have to respect inequality operators
def rule_6(grid: Futoshiki):
	clauses = []
	for i, j in grid.inequality:
		small, big = grid.get_cell_from_id(i), grid.get_cell_from_id(j)
		clauses += [(-small[grid.side],)]
		clauses += [(-big[1],)]
		for x in range(2, grid.side+1):
			clauses += [tuple([-big[x]] + [small[y] for y in range(x-1, 0, -1)])]
	return clauses


# Create .cnf file using DIMACS conventions
def create_cnf(filename: str, side: int, *args):
	lines = list(it.chain(*args))
	lines = list(map(lambda x: ' '.join(list(map(lambda x: str(x), x)))+' 0\n', lines))
	print(lines)
	with open(filename, "w") as file:
		file.write(f"p cnf {side**3} {len(lines)}\n")
		file.writelines(lines)
