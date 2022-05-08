import pysat


# Use the sat file to create a list of the solution
def resolution(sat_file):
	# WIP
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
