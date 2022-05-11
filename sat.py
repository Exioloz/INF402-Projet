from pysat.formula import CNF
from pysat.solvers import Minisat22


# Use the .cnf to SAT-solve it
def sat_solve(cnf_file, sat_file):
	cnf = CNF(from_file=cnf_file)  # reading from the cnf

	# Solving and get the sat model using 'Minisat22' with the cnf clauses
	with Minisat22(bootstrap_with=cnf) as m:
		m.solve()
		model = m.get_model()
		sat_file.write(str(model))  # Writing the SAT model in a corresponding file
	return model  # SAT-solved list of boolean


# Use the SAT-solved file to create a list of the solution
def resolution(n, sat):

	# Keeping only positive bools && Finding the futoshiki answers for each cell
	solution = []
	for number in sat:
		if number > 0:
			# The solution is the rest of the division of the X of the positive bool and the size of the puzzle
			cell_number = number % n
			if cell_number == 0:  # When the rest is 0 the maximum number that the futoshiki can hold is the answer
				cell_number = n
			solution.append(cell_number)
	return solution


# Create file with the completed Futoshiki.
def create_solution(futoshiki, complete, solution):

	size = int(futoshiki[0])  # The n size of an n*n futoshiki
	index_futoshiki = 2  # The first two characters of the futoshiki file are the size and '\n'
	complete.write(futoshiki[0])
	complete.write(futoshiki[1])

	index_solution = 0  # Keeping track of the solution (first digits start for the top left cell of the puzzle)
	# Constant line and row size for each .futoshiki file excluding the first line
	line_size = size * 4 - 2  # The number of characters present on each line
	row_size = size + size - 1  # The number of characters present on each row

	line_with_cell = 0  # Keeping track of which line contain numbers
	# Going through each line of the futoshiki file
	for line in range(row_size):
		row_with_cell = 0  # Keeping track of which row contain numbers
		line_change = 0  # Boolean flag to know if the current line has numbers
		# Going through each row of the futoshiki file for the current line
		for row in range(line_size):
			# When the current and current line correspond to a number cell then we write the real answer instead.
			if row == row_with_cell and line == line_with_cell:
				row_with_cell += 4  # Each number is seperated by 4 row on every line
				line_change = 1
				complete.write(str(solution[index_solution]))
				index_solution += 1  # After writing one answer we move to the next one in the solution
			# Else we rewrite the incomplete futoshiki
			else:
				complete.write(futoshiki[index_futoshiki])
			index_futoshiki += 1  # Even if we do not write from the incomplete file with move to its next character

		if line_change:
			line_with_cell += 2  # Each number is seperated by 2 line on every row
