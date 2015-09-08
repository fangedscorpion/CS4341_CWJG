""" Class for Heuristic functions """

class Heuristic(object):
	# function is an integer representing the specific huersitic function
	def __init__(self, function):
		self.function = function

	# This function returns the integer representing the specific heuristic function
	# INPUT -> none
	# OUTPUT -> (int) function
	def getFunction(self):
		return self.function

	# This function returns the heuristic evaluation for heuristic 1
	# heuristic 1 is always 0
	# INPUT -> (Cell) the cell being evaluated
	# OUTPUT -> (int) 0
	def heur1(self, a_cell):
		return 0

if __name__ == "__main__":
	a_h = Heuristic(4)
	print a_h.heur1("test cell")