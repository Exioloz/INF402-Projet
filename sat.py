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

	n = len(solution)
	y = 1
	completed_futoshiki.write(solution[0])
	for x in range(1, n-2):
		completed_futoshiki.write(solution[x])
		completed_futoshiki.write(futoshiki[x + 1])
		completed_futoshiki.write(futoshiki[x + 2])
		completed_futoshiki.write(futoshiki[x + 3])

		if x == n/y:
			i = 0
			while i < n:
				completed_futoshiki.write(" ")
				i += 1
			y += 1

	completed_futoshiki.write(solution[n-1])
	completed_futoshiki.close()
