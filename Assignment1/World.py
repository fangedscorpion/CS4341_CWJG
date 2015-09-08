""" World Class """
""" Representation of all cells in the World """

class World(object):
	# file is the input world file
	# MakeWorld parses the input file and creates a list of a list of cells
	# self.start stores the starting cell to avoid using the function getStart() repeatidly
	# self.goal stores the goal cell to avoid using the function getGoal() repeatidly
	def __init__(self, file):
		self.file = file
		self.world = MakeWorld(self.file)
		self.start = getStart()
		self.goal = getGoal()

	# parses the input file and creates the world
	# INPUT -> (file) input world
	# OUTPUT -> (list of list of Cells) formatted world
	def MakeWorld(file)
		lines = file.readlines()

		for j in range(0, len(lines)):
			fixed.append(lines[j].split)

		for k in range(0, len(fixed)):
			for l in range(0, len(fixed[k])):
				# world[l][k] = Cell(fixed[k][l])
				world[l][k] = fixed[k][l] # this line is for debugging, replace with line above when Cell is defined

		return world

