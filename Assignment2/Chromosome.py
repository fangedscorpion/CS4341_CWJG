class Chromosome(object):
    def __init__(self, gen):
        self.generation = gen

    # This method initializes the chromosome for generation 0
    def initialize(self):
        self.generation = 0

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
