import random as rand

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
