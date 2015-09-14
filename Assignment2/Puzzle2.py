from Chromosome import *
class Puzzle2(Chromosome):

    def __init__(self, bin1List, bin2List, bin3List, generation):
        super(Puzzle2, self).__init__(generation)
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

    def __repr__(self):
        return ("Bin1: " + str(self.bin1) + "\nBin2: " + \
                str(self.bin2) + "\nBin3: " + str(self.bin3) + "\n")

if __name__ == '__main__':
    from Puzzle2 import Puzzle2
    a = [1,0,-6,-9.9,8,4.5,3,3.8,2.5]
    par1 = Puzzle2(a[0:3], a[3:6], a[6:9], 0)
    par2 = Puzzle2(a[3:6], a[0:3], a[6:9], 0)
    par3 = Puzzle2(a[6:9], a[3:6], a[0:3], 0)
    par4 = Puzzle2(a[6:9], a[0:3], a[3:6], 0)

    print par1
    print par2
    print par3
    print par4

    print par1.getGeneration()

