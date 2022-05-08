import pysat


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
def resolution(sat_file):

	# WIP
	with open(sat_file, "r") as sat:
		lines = sat.readlines()

	# Trying to transform string to int from lines to int_tab
	int_tab = []
	for line in lines:
		int_tab.append(int(line))

	sat_sol = []
	for number in int_tab:
		if number > 0:
			sat_sol.append(number)
	# Transform the x(a) to the actual answer
	# TODO
	solution = []
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
