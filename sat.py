from pysat.formula import CNF
from pysat.solvers import Minisat22


# Use the .cnf to SAT-solve it
def sat_solve(cnf_file, sat_file):
	cnf = CNF(from_file=cnf_file)  # reading from file
	sat_tab = []
	with Minisat22(bootstrap_with=cnf) as m:
		m.solve()
		m.get_model()
		sat_tab.append(m.get_model())
		sat_file.write(str(m.get_model()))
	return sat_tab[0]


# Use the SAT-solved file to create a list of the solution
def resolution(n, sat):

	# Keeping only positive bools
	positive_bool = []
	for number in sat:
		if number > 0:
			positive_bool.append(number)

	# Finding the futoshiki answers for each cell
	solution = []
	for number in positive_bool:
		c = number % n
		if c == 0:
			c = n
		solution.append(c)
	return solution


# Create file with the solved Futoshiki.
def create_solution(futoshiki, complete, solution):

	complete.write(futoshiki[0])
	complete.write(futoshiki[1])

	size = int(futoshiki[0])
	index_futoshiki = 2
	index_sol = 0
	line_size = size * 4 - 2
	row_size = size + size
	j = 0
	
	for row in range(row_size - 1):
		i = 0
		add_j = 0
		for line in range(line_size):
			if line == i and row == j:
				i += 4
				add_j = 1
				complete.write(str(solution[index_sol]))
				index_sol += 1
			else:
				complete.write(futoshiki[index_futoshiki])
			index_futoshiki += 1
		if add_j:
			j += 2
