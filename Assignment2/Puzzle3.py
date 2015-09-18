class Puzzle3(object):
    def __init__(self, gen):
        super(Puzzle3, self).__init__(gen)
        self.mutationThreshold = 50  # Percentage of 100 for each digit

    # This method initializes the chromosome for generation 0
    # jake
    def initialize(self, masterList):
        super(Puzzle3, self).__init__(0)
        self.towerList = XXXX # Ind 0 = Bottom 
        # Height = len(towerList)

    # This method checks if a chromosome is legal
    # jake
    def checkLegality(self):
        pass

    # This method does a crossover for multiple chromosomes
    # chas
    def crossover(self):
        pass

    # this function evaluates the fitness of a chromosome
    # jake
    def fitness(self):
        pass

    # this funcction mutates a chromosome
    # chas
    def mutate(self):
        pass

    def getGeneration(self):
        return self.generation
