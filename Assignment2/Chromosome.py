import abc


class Chromosome(object):
    __metaclass__ = abc.ABCMeta

    # This method initializes the chromosome for generation 0
    @abc.abstractmethod
    def initialize(self):
        pass

    # This method checks if a chromosome is legal
    @abc.abstractmethod
    def checkLegality(self):
        pass

    # This method does a crossover for multiple chromosomes
    @abc.abstractmethod
    def crossover(self):
        pass

    # this function evaluates the fitness of a chromosome
    @abc.abstractmethod
    def fitness(self):
        pass

    @abc.abstractmethod
    def getCopy(self):
        return "ERROR! must be implemented"

    # this funcction mutates a chromosome
    @abc.abstractmethod
    def mutate(self):
        pass

    @abc.abstractmethod
    def getGeneration(self):
        pass
