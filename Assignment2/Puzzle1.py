import Chromosome
class Puzzle2(Chromosome):

	def __init__(self, bin1List, bin2List, bin3List):
		self.bin1 = bin1List
		self.bin2 = bin2List
		self.bin3 = bin3List

    # This method initializes the Puzzle for generation 0
    def initialize(self):
    	pass

    # This method checks if a Puzzle is legal
    def checkLegality(self):
    	pass

    # This method does a crossover for multiple Puzzles
    def crossover(self, other):
    	pass

    # this function evaluates the fitness of a Puzzle
    def fitness(self):
    	pass

    # this funcction mutates a Puzzle
    def mutate(self):
    	pass