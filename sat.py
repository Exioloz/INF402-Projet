# Use the .cnf to SAT-solve it
def sat_solve(cnf_file, sat_file):

	# WIP
	cnf = open(cnf_file, "r")
	sat = open(sat_file, "w")

	# Use of PySat to SAT-Solve
	# TODO
	# sol = pysat.formatter(cnf) ?
	sol = "0"
	sat.write(sol)

	cnf.close()
	sat.close()


# Use the SAT-solved file to create a list of the solution
def resolution(n, sat_file):
	f_sat = open(sat_file, "r")

	# Keeping only positive bools
	number_tab = []
	minus = 0
	number = ""
	tab = f_sat.read()
	for char in tab:
		if char == " ":
			if minus == 0:
				number_tab.append(number)
			minus = 0
			number = ""
		else:
			if char == "-":
				minus = 1

			if minus == 0:
				number = number + char

	# Transforming str to int
	int_tab = []
	for x in number_tab:
		int_tab.append(int(x))
	print(int_tab)

	# Finding the futoshiki answers for each cell
	solution = []
	for number in int_tab:
		c = number % n
		if c == 0:
			c = 3
		solution.append(c)

	return solution


# Create file with the solved Futoshiki.
def create_solution(file_in, file_out, solution):
	base = open(file_in, "r")
	futoshiki = base.read()
	base.close()

	complete = open(file_out, "w")
	complete.write(futoshiki[0])
	complete.write(futoshiki[1])

	size = int(futoshiki[0])
	index_futoshiki = 2
	index_sol = 0
	line_size = size * size  # 9
	row_size = size + size  # 6
	print(row_size)
	print(line_size)
	j = 0

	for row in range(row_size - 1):
		i = 0
		add_j = 0
		for line in range(line_size + 1):
			print("line:", line, " i :", i)
			# print("row :",row, " j :", j)
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
