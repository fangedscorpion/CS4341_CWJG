from abc import ABCMeta, abstractmethod

class Abstract(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def initialize(self):
    	pass

    @abstractmethod
    def checkLegality(self):
    	pass

    @abstractmethod
    def crossover(self):
    	pass

    @abstractmethod
    def fitness(self):

    @abstractmethod
    def mutate(self):
    	pass

if __name__ == "__name__":
	abbbb = Abstract()