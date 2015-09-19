import random as rand
import copy
from Piece import Piece
from Chromosome import Chromosome

class Puzzle3(Chromosome):
    def __init__(self, gen):
        super(Puzzle3, self).__init__(gen)
        self.mutationThreshold = 50  # Percentage of 100 for each digit
        self.height = -1
        self.towerList = []

    # This method initializes the chromosome for generation 0
    # jake
    def initialize(self, masterList):
        super(Puzzle3, self).__init__(0)
        size = rand.randint(2, len(masterList))

        new_masterList = copy.copy(masterList)

        for j in range(0, size):
            a_piece = new_masterList[rand.randint(0, len(new_masterList) - 1)]
            new_masterList.remove(a_piece)
            self.towerList.append(a_piece)

        self.height = len(self.towerList)

    # This method checks if a chromosome is legal
    # jake
    def checkLegality(self):
        pass

    # This method does a crossover for multiple chromosomes
    # chas
    def crossover(self, other):
        thisList = self.towerList
        otherList = other.getTowerList()
        
        rand1Num = rand.randint(1, len(thisList) - 1)
        rand2Num = rand.randint(1, len(otherList) - 1)

        self.towerList = list(thisList[0:rand1Num], otherList[rand2Num:len(otherList)])
        other.setTowerList(list(otherList[0:rand2Num], thisList[rand1Num:len(thisList)]))

    # this function evaluates the fitness of a chromosome
    # jake
    def fitness(self):
        pass

    # this funcction mutates a chromosome
    # chas
    def mutate(self, masterList):
        for x in range(len(self.towerList)):
            randPerc = rand.randint(1, 100)

            if(randPerc <= self.mutationThreshold):
                randInt = rand.randint(0, len(masterList)-1)

                newPart = masterList[randInt]

                if(not newPart in self.towerList):
                    self.towerList[x] = newPart
            else:
                pass

    def getTowerList(self):
        return self.towerList

    def setTowerList(self, towerList):
        self.towerList = towerList

    def getGeneration(self):
        return self.generation

if __name__ == "__main__":
    a = [1,2,3,4,5,6,7,8,9]
    alpha = Puzzle3(0)
    beta = Puzzle3(0)
    alpha.initialize(a)
    beta.initialize(a)

    print alpha.towerList
    print beta.towerList