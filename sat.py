from pysat.solvers import CNF
from pysat.solvers import Minisat22


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
		solution.append((number % n) + 1)
	return solution


# Create file with the solved Futoshiki.
def create_solution(file_in, file_out, solution):

	empty_futoshiki = open(file_in, "r")
	completed_futoshiki = open(file_out, "w")
	futoshiki = empty_futoshiki.read()
	empty_futoshiki.close()
	completed_futoshiki.write(futoshiki[0])
	completed_futoshiki.write("\n")

	size = int(futoshiki[0])
	n = len(solution)
	x = 1  # lines with the futoshiki cells
	i = 0
	for row in range(1, size*2):
		y = 1  # rows with the futoshiki cells

		for line in range(1, size*size):
			completed_futoshiki.write(futoshiki[(row * line)])
			if line == y and row == x:
				if i >= n:
					print("Erreur solution et futoshiki incompatible")
				completed_futoshiki.write(solution[i])
				i += 1
				y += 4  # 3 spaces before next cell
		x += 2  # 1 line before next cell
		completed_futoshiki.write("\n")
	completed_futoshiki.close()
