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

    def getBin1(self):
        return self.bin1

    def getBin2(self):
        return self.bin2

    def getBin2(self):
        return self.bin3

if __name__ == '__main__':
    from Puzzle2 import Puzzle2
    a = [1 0 -6 -9.9 8 4.5 3 3.8 2.5]
    par1 = Puzzle2(a[0:2], a[3:5], a[6:8])
    par2 = Puzzle2(a[3:5], a[0:2], a[6:8])
    par3 = Puzzle2(a[6:8], a[3:5], a[0:2])
    par4 = Puzzle2(a[6:8], a[0:2], a[3:5])