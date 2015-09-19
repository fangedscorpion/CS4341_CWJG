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
        # 0
        if (not (len(self.towerList) >= 2)):
            return False

        # 1
        if (not (self.towerList[0].isDoor())):
            return False
        # 2
        if (not (self.towerList[len(self.towerList) - 1].isLookout())):
            return False

        # 3
        for j in range(1, len(self.towerList) - 1):
            if (not (self.towerList[0].isWall())):
                return False

        # 4
        for k in range(1, len(self.towerList)):
            if (self.towerList[k].canFit(self.towerList[k - 1]) == False):
                return False

        # 5
        for l in range(0, len(self.towerList) - 1):
            if (self.towerList[l].canSupportNum(len(self.towerList[l::])) == False):
                return False

        return True

        # This method does a crossover for multiple chromosomes
        # chas
    def crossover(self, other):
        thisList = self.towerList
        otherList = other.getTowerList()

        rand1Num = rand.randint(1, len(thisList) - 1)
        rand2Num = rand.randint(1, len(otherList) - 1)

        self.towerList = list(
            thisList[0:rand1Num], otherList[rand2Num:len(otherList)])
        other.setTowerList(
            list(otherList[0:rand2Num], thisList[rand1Num:len(thisList)]))

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
                randInt = rand.randint(0, len(masterList) - 1)

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

if __name__ == '__main__':
    from Piece import Piece
    d1 = Piece("Door", 5, 2, 2, 0)
    w1 = Piece("Wall", 5, 5, 1, 1)
    w2 = Piece("Wall", 4, 3, 1, 2)
    d2 = Piece("Door", 3, 5, 2, 3)
    w3 = Piece("Wall", 3, 3, 2, 4)
    l1 = Piece("Lookout", 2, 2, 3, 5)
    l2 = Piece("Lookout", 3, 1, 2, 6)
    l3 = Piece("Lookout", 3, 1, 2, 7)
    masterList = [d1, w1, w2, d2, w3, l1, l2, l3]

    ap3a = Puzzle3(0)
    ap3b = Puzzle3(0)
    ap3c = Puzzle3(0)
    ap3d = Puzzle3(0)
    ap3e = Puzzle3(0)
    ap3f = Puzzle3(0)

    alpha = Puzzle3(0)
    beta = Puzzle3(0)
    gamma = Puzzle3(0)
    delta = Puzzle3(0)
    epsilon = Puzzle3(0)
    zeta = Puzzle3(0)
    eta = Puzzle3(0)


    genY = [ap3a, ap3b, ap3c, ap3d, ap3d, ap3e, ap3f, alpha, beta]

    for chromo in genY:
        chromo.initialize(masterList)
        print chromo.towerList

    # 0
    alpha.towerList = [w1]
    # 1
    beta.towerList = [w1, w2, d2, l1]
    # 2
    gamma.towerList = [d1, w1, w2]
    # 3
    delta.towerList = [d1, d2, l1]
    # 4
    epsilon.towerList = [d2, w1, l1]
    # 5
    zeta.towerList = [d1, w1, w2, w3, l1]
    # 6
    eta.towerList = [d1, l1]

    print alpha.checkLegality(), False
    print beta.checkLegality(), False
    print gamma.checkLegality(), False
    print delta.checkLegality(), False
    print epsilon.checkLegality(), False
    print zeta.checkLegality(), False
    print eta.checkLegality(), True