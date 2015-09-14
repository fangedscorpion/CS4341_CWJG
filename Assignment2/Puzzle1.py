import Chromosome
class Puzzle1(Chromosome):

    def __init__(self, listOfNum):
        self.lon = listOfNum

    # This method initializes the Puzzle for generation 0
    def initialize(self):
        pass

    # This method checks if a Puzzle is legal
    def checkLegality(self):
        pass

    # This method does a crossover for multiple Puzzles
    def crossover(self, other):
        

    # this function evaluates the fitness of a Puzzle
    def fitness(self):
        pass

    # this funcction mutates a Puzzle
    def mutate(self):
        pass

    def getListOfNum(self):
        return self.lon


if __name__ == '__main__':


