from abc import ABCMeta, abstractmethod

class Abstract(object):
    __metaclass__ = ABCMeta

    # This method initializes the chromosome for generation 0
    @abstractmethod
    def initialize(self):
    	pass

    # This method checks if a chromosome is legal
    @abstractmethod
    def checkLegality(self):
    	pass

    # This method does a crossover for multiple chromosomes
    @abstractmethod
    def crossover(self):
    	pass

    # this function evaluates the fitness of a chromosome
    @abstractmethod
    def fitness(self):
    	pass

    # this funcction mutates a chromosome
    @abstractmethod
    def mutate(self):
    	pass
