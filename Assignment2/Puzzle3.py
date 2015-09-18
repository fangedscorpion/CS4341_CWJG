class Puzzle3(object):
    def __init__(self, gen):
        super(Puzzle3, self).__init__(generation)
        self.bin1 = bin1List
        self.bin2 = bin2List
        self.bin3 = bin3List

        self.mutationThreshold = 50  # Percentage of 100 for each digit

    # This method initializes the chromosome for generation 0
    def initialize(self):
        super(Puzzle3, self).__init__(0)

    # This method initializes the chromosome for generation 0
    def initialize(self):
        pass

    # This method checks if a chromosome is legal
    def checkLegality(self):
        pass

    # This method does a crossover for multiple chromosomes
    def crossover(self):
        pass

    # this function evaluates the fitness of a chromosome
    def fitness(self):
        pass

    # this funcction mutates a chromosome
    def mutate(self):
        pass

    def getGeneration(self):
        return self.generation
