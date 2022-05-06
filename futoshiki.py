import numpy as np

class Cell:
	def __init__(self, i: int, j: int, side:int):
		self.id = i * side + j
		self.side = side
		self.booleans = np.array(range(self.id * side + 1, self.id * side + 1 + side))
		self.value = 0

	def __repr__(self):
		return f'Cell({self.value=}, {self.booleans=})'

	def __str__(self):
		return 'x' if self.value == 0 else str(self.value)

	def __getitem__(self, i):
		assert 0 < i <= self.side
		return self.booleans[i-1]
		
	def set_value(self, value):
		assert 0 <= value <= self.side
		self.value = value

class Futoshiki:
	def __init__(self, filename: str):
		# Reading file content
		with open(filename, 'r') as file:
			content = file.readlines()
		
		# Getting the size of grid side
		self.side = int(content[0])
		
		# Creating grid of default valuated cells
		self.grid = [[Cell(i, j, self.side) for j in range(0, self.side)] for i in range(0, self.side)]
		
		# Parsing the read content to update cells that have pre-assigned values
		for line in self.grid:
			for cell in line:
				cell.set_value(int(content[1 + (cell.id // self.side) * 2][(cell.id % self.side) * 4]))
		
		# Parsing the read content to store inequality relations between cells (by cell id)
		# Stored as tuple(a, b), where: cell a < cell b
		self.inequality = []
		for i, line in enumerate(content[1:]):
			if i % 2 == 0:
				for j, sym in enumerate(line[2::4]):
					if sym == "<":
						self.inequality.append((i//2 * self.side + j, i//2 * self.side + j + 1))
					if sym == ">":
						self.inequality.append((i//2 * self.side + j + 1, i//2 * self.side + j))
			else:
				for j, sym in enumerate(line[0::4]):
					if sym == "^":
						self.inequality.append(((i-1)//2 * self.side + j, (i+1)//2 * self.side + j))
					if sym == "v":
						self.inequality.append(((i+1)//2 * self.side + j, (i-1)//2 * self.side + j))

	def __getitem__(self, i):
		return self.grid[i]

	def get_cell_from_id(self, id):
		return self.grid[(id // self.side)][id % self.side]

	def print(self):
		for line in self.grid:
			for cell in line:
				print(cell, end='   ')
			print(end='\n\n')
