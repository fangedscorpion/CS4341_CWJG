from Chromosome import *
import random as rand
class Puzzle2(Chromosome):

    def __init__(self, bin1List, bin2List, bin3List, generation):
        super(Puzzle2, self).__init__(generation)
        self.bin1 = bin1List
        self.bin2 = bin2List
        self.bin3 = bin3List

        self.mutationThreshold = 50 # Percentage of 100 for each digit

    # This method initializes the Puzzle for generation 0
    def initialize(self):
        super(Puzzle2, self).__init__(0)

    # This method checks if a Puzzle is legal
    def checkLegality(self):
        pass

    # This method does a crossover for multiple Puzzles
    def crossover(self, other):
        pass

    # this function evaluates the fitness of a Puzzle
    def fitness(self):
        pass

    def getValidMutatedNumber(self):
        # Consult dictionary here
        return rand.randint(1, 50)

    def fixChild(self, listOfChangedNums):
        print listOfChangedNums

        for x in range(0, (len(listOfChangedNums)-1), 2):
            # Generate another rand int in size of changed list
            ind1 = rand.randint(0, (len(listOfChangedNums)-1))
            ind2 = rand.randint(0, (len(listOfChangedNums)-1))
            while(ind2 == ind1):
                ind2 = rand.randint(0, (len(listOfChangedNums)-1))
            print ind1,ind2

            changedTuple1 = listOfChangedNums[ind1]
            changedTuple2 = listOfChangedNums[ind2]

            #Swap values
            if(changedTuple1[0] == 1):
                self.bin1[changedTuple1[1]] = changedTuple2[2]
            elif(changedTuple1[0] == 2):
                self.bin2[changedTuple1[1]] = changedTuple2[2]
            elif(changedTuple1[0] == 3):
                self.bin3[changedTuple1[1]] = changedTuple2[2]

            if(changedTuple2[0] == 1):
                self.bin1[changedTuple2[1]] = changedTuple1[2]
            elif(changedTuple2[0] == 2):
                self.bin2[changedTuple2[1]] = changedTuple1[2]
            elif(changedTuple2[0] == 3):
                self.bin3[changedTuple2[1]] = changedTuple1[2]

            listOfChangedNums.remove(changedTuple2)
            listOfChangedNums.remove(changedTuple1)

        if(len(listOfChangedNums) == 1):
            lastChangedTuple = listOfChangedNums[0]
            if(lastChangedTuple[0] == 1):
                self.bin1[lastChangedTuple[1]] = lastChangedTuple[2]
            elif(lastChangedTuple[0] == 2):
                self.bin2[lastChangedTuple[1]] = lastChangedTuple[2]
            elif(lastChangedTuple[0] == 3):
                self.bin3[lastChangedTuple[1]] = lastChangedTuple[2]

    # this funcction mutates a Puzzle
    # It goes through all three at once and mutates if the number is between 1 and 8
    # If so it gets added to spareNums as a tuple with the changed index and the bin #
    # The fixChild class then makes the kid legal
    def mutate(self):
        spareNums = []
        for x in range(0,len(self.bin1)):
            l1Rand = rand.randint(1,100)
            l2Rand = rand.randint(1,100)
            l3Rand = rand.randint(1,100)


            if(l1Rand <= self.mutationThreshold):
                spareNums.append([1, x, self.bin1[x]])
                self.bin1[x] = self.getValidMutatedNumber()

            if(l2Rand <= self.mutationThreshold):
                spareNums.append([2, x, self.bin2[x]])
                self.bin2[x] = self.getValidMutatedNumber()

            if(l3Rand <= self.mutationThreshold):
                spareNums.append([3, x, self.bin3[x]])
                self.bin3[x] = self.getValidMutatedNumber()

        self.fixChild(spareNums)

    def getBin1(self):
        return self.bin1

    def getBin2(self):
        return self.bin2

    def getBin2(self):
        return self.bin3

    def __repr__(self):
        return ("Bin1: " + str(self.bin1) + "\nBin2: " + \
                str(self.bin2) + "\nBin3: " + str(self.bin3) + "\n")

if __name__ == '__main__':
    from Puzzle2 import Puzzle2
    a = [1,0,-6,-9.9,8,4.5,3,3.8,2.5]
    par1 = Puzzle2(a[0:3], a[3:6], a[6:9], 0)
    par2 = Puzzle2(a[3:6], a[0:3], a[6:9], 0)
    par3 = Puzzle2(a[6:9], a[3:6], a[0:3], 0)
    par4 = Puzzle2(a[6:9], a[0:3], a[3:6], 0)

    print par1
    print par2
    print par3
    print par4

    par4.mutate()

    print par4

    print "Generation 0?: ", par1.getGeneration()

