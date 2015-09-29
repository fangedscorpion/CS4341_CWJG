from Chromosome import *
import random as rand
from Illegal import Illegal
from Location import Location
import copy


class Puzzle2(Chromosome):

    def __init__(self, bin1List, bin2List, bin3List, generation, mutation):
        self.generation = generation
        self.bin1 = bin1List
        self.bin2 = bin2List
        self.bin3 = bin3List

        self.mutationThreshold = mutation  # Percentage of 100 for each digit

    # This method initializes the Puzzle for generation 0
    # master is a list of all possible floats to create a Puzzle2 from
    def initialize(self, master):
        self.generation = 0
        new_master = copy.copy(master)

        top = len(new_master) / 3

        for j in range(0, 3):
            for k in range(0, top):
                number = float(
                    new_master[rand.randint(0, len(new_master) - 1)])
                new_master.remove(number)

                if (j == 0):
                    self.bin1.append(number)
                elif (j == 1):
                    self.bin2.append(number)
                elif (j == 2):
                    self.bin3.append(number)
                else:
                    print "oh no"

    # This method checks if a Puzzle is legal
    # INPUT -> (dict) master dictionary
    # OUTPUT -> (boolean) True
    #           (list of Illegal) information about problems
    def checkLegality(self, master):
        # create new dict from master
        thisDict = master.copy()

        childDict = self.countInDict({})

        immigrationList = []
        deportationList = []
        childDictCopy = childDict.copy()

        for x in master.keys():
            if(childDictCopy.has_key(x)):
                if(not (childDictCopy[x][0] == master[x])):

                    diffCount = master[x] - childDictCopy[x][0]
                    if(diffCount > 0):
                        for ind in range(0, diffCount):
                            immigrationList.append(Illegal(x, 0, []))

                    if(diffCount < 0):
                        diffCount = abs(diffCount)
                        tmpList = list(childDictCopy[x][1])
                        for ind in range(0, diffCount):
                            randInd = rand.randint(0, len(tmpList) - 1)
                            deportationList.append(
                                Illegal(x, diffCount, tmpList[randInd]))
                            tmpList.remove(tmpList[randInd])
            else:
                for i in range(0, master[x]):
                    immigrationList.append(Illegal(x, 0, []))

        # These lists should be the same size
        return (len(deportationList) == 0 and len(immigrationList) == 0, deportationList, immigrationList)

    def fixChild(self, masterDictionary):

        thisDict = masterDictionary.copy()

        childDict = self.countInDict({})

        immigrationList = []
        deportationList = []
        childDictCopy = childDict.copy()

        for x in masterDictionary.keys():
            if(childDictCopy.has_key(x)):
                if(not (childDictCopy[x][0] == masterDictionary[x])):

                    diffCount = masterDictionary[x] - childDictCopy[x][0]
                    if(diffCount > 0):
                        for ind in range(0, diffCount):
                            immigrationList.append(Illegal(x, 0, []))

                    if(diffCount < 0):
                        diffCount = abs(diffCount)
                        tmpList = list(childDictCopy[x][1])
                        for ind in range(0, diffCount):
                            randInd = rand.randint(0, len(tmpList) - 1)
                            deportationList.append(
                                Illegal(x, diffCount, tmpList[randInd]))
                            tmpList.remove(tmpList[randInd])
            else:
                for i in range(0, masterDictionary[x]):
                    immigrationList.append(Illegal(x, 0, []))

        self.fixChildGivenLists(deportationList, immigrationList)

    # This function forms a counting dictionary from the values in a Puzzle2
    # If a value in a Puzzle2 is not a key in the dictionary,
    # the unknown value is printed AND added to the list
    # INPUT -> (dict) empty dict
    # OUTPUT -> (dict) counted dict
    def countInDict(self, starting):
        # print "%" * 20
        for i in range(0, len(self.bin1)):
            if (starting.has_key(self.bin1[i])):
                starting[self.bin1[i]] = (
                    starting[self.bin1[i]][0] + 1, list(starting[self.bin1[i]][1] + [Location(1, i)]))
            else:
                starting[self.bin1[i]] = (1, [Location(1, i)])
            if (starting.has_key(self.bin2[i])):
                starting[self.bin2[i]] = (
                    starting[self.bin2[i]][0] + 1, list(starting[self.bin2[i]][1] + [Location(2, i)]))
            else:
                starting[self.bin2[i]] = (1, [Location(2, i)])

            if (starting.has_key(self.bin3[i])):
                starting[self.bin3[i]] = (
                    starting[self.bin3[i]][0] + 1, list(starting[self.bin3[i]][1] + [Location(3, i)]))
            else:
                starting[self.bin3[i]] = (1, [Location(3, i)])

        return starting

    # This fixChild method makes a valid Puzzle2 chromosome from
    # an incorrect one and two lists of values that need to be swapped
    # One list is the values that need to be added into the object
    # The other list has the values that need to be moved out of the object
    def fixChildGivenLists(self, exportList, importList):
        assert len(importList) == len(exportList)

        for x in range(0, len(importList)):
            randint = rand.randint(0, len(importList) - 1)
            randint2 = rand.randint(0, len(exportList) - 1)

            importedIllegalObj = importList[randint]
            exportedIllegalObjLoc = exportList[randint2].getLocations()

            if(exportedIllegalObjLoc.getBin() == 1):
                self.bin1[
                    exportedIllegalObjLoc.getIndex()] = importedIllegalObj.getValue()
                del importList[randint]
                del exportList[randint2]
            elif(exportedIllegalObjLoc.getBin() == 2):
                self.bin2[
                    exportedIllegalObjLoc.getIndex()] = importedIllegalObj.getValue()
                del importList[randint]
                del exportList[randint2]
            elif(exportedIllegalObjLoc.getBin() == 3):
                self.bin3[
                    exportedIllegalObjLoc.getIndex()] = importedIllegalObj.getValue()
                del importList[randint]
                del exportList[randint2]

        assert len(importList) == 0
        assert len(exportList) == 0

    # This method does a crossover for multiple Puzzles
    def crossover(self, other):
        cutPointInt = rand.randint(1, (len(self.bin1) - 1))

        # up to but not including the cutPointInt
        par1Bin1Front = self.bin1[0:cutPointInt]
        par1Bin2Front = self.bin2[0:cutPointInt]
        par1Bin3Front = self.bin3[0:cutPointInt]

        # up to but not including the cutPointInt
        par2Bin1Front = other.bin1[0:cutPointInt]
        par2Bin2Front = other.bin2[0:cutPointInt]
        par2Bin3Front = other.bin3[0:cutPointInt]

        # up to but not including the end length
        par1Bin1End = self.bin1[cutPointInt:len(self.bin1)]
        par1Bin2End = self.bin2[cutPointInt:len(self.bin2)]
        par1Bin3End = self.bin3[cutPointInt:len(self.bin3)]

        # up to but not including the end length
        par2Bin1End = other.bin1[cutPointInt:len(other.bin1)]
        par2Bin2End = other.bin2[cutPointInt:len(other.bin2)]
        par2Bin3End = other.bin3[cutPointInt:len(other.bin3)]

        newPa = Puzzle2(
            [], [], [], self.generation + 1, self.mutationThreshold)
        newPb = Puzzle2(
            [], [], [], other.generation + 1, other.mutationThreshold)

        par1Bin1Front.extend(par2Bin1End)
        newPa.bin1 = par1Bin1Front
        par1Bin2Front.extend(par2Bin2End)
        newPa.bin2 = par1Bin2Front
        par1Bin3Front.extend(par2Bin3End)
        newPa.bin3 = par1Bin3Front

        par2Bin1Front.extend(par1Bin1End)
        newPb.bin1 = par2Bin1Front
        par2Bin2Front.extend(par1Bin2End)
        newPb.bin2 = par2Bin2Front
        par2Bin3Front.extend(par1Bin3End)
        newPb.bin3 = par2Bin3Front

        return (newPa, newPb)

    # this function evaluates the fitness of a Puzzle
    # fitness = product(bin1) + sum(bin2)
    def fitness(self, diction, target):
        if (self.checkLegality(diction)):
            bProd = 1
            bSum = 0

            # because  for a Puzzle2 to be legal, all bins must be the same size
            # therefore, 1 for loop can be used
            for j in range(0, len(self.bin1)):
                bProd *= self.bin1[j]
                bSum += self.bin2[j]

            return (bProd + bSum) / 2
        else:
            return 0

    def getValidMutatedNumberIndex(self, lenMasterListOfNum):
        return rand.randint(0, (lenMasterListOfNum - 1))

    # this function mutates a Puzzle
    # It goes through all three at once and mutates if the number is between 1 and 8
    # If so it gets added to spareNums as a tuple with the changed index and the bin #
    # The fixChild class then makes the kid legal
    def mutate(self, masterListOfNum, masterDict):
        spareNums = []
        for x in range(0, len(self.bin1)):
            l1Rand = rand.randint(1, 100)
            l2Rand = rand.randint(1, 100)
            l3Rand = rand.randint(1, 100)

            if(l1Rand <= self.mutationThreshold):
                spareNums.append([1, x, self.bin1[x]])
                self.bin1[x] = masterListOfNum[
                    self.getValidMutatedNumberIndex(len(masterListOfNum))]

            if(l2Rand <= self.mutationThreshold):
                spareNums.append([2, x, self.bin2[x]])
                self.bin2[x] = masterListOfNum[
                    self.getValidMutatedNumberIndex(len(masterListOfNum))]

            if(l3Rand <= self.mutationThreshold):
                spareNums.append([3, x, self.bin3[x]])
                self.bin3[x] = masterListOfNum[
                    self.getValidMutatedNumberIndex(len(masterListOfNum))]

        self.fixChild(masterDict)

    def getBin1(self):
        return self.bin1

    def getBin2(self):
        return self.bin2

    def getBin3(self):
        return self.bin3

    def getGeneration(self):
        return self.generation

    def getCopy(self):
        tempChromeo = Puzzle2(list(self.getBin1()), list(self.getBin2()), list(
            self.getBin3()), self.getGeneration(), self.mutationThreshold)
        return tempChromeo

    def __repr__(self):
        return ("Bin1: " + str(self.bin1) + "\nBin2: " +
                str(self.bin2) + "\nBin3: " + str(self.bin3) + " Gen: " + str(self.generation))

Chromosome.register(Puzzle2)

if __name__ == '__main__':
    a = [-6.3, -9.9, -3.0, 4.0, 0.0, 2.5, 8.8, 0.6, -4.5, 2.3, -5.0, 7.0, 2.5, 4.5, -
         6.0, 8.0, 7.5, 6.5, 2.0, -1.0, -0.5, 0.0, 3.3, 8.2, 1.5, 9.2, -7.0, 2.5, 6.2, -2.2]

    adict = {0.0: 2, 2.5: 3, 2.0: 1, 4.0: 1, 7.5: 1, 7.0: 1, 8.0: 1, 3.3: 1, 8.2: 1, -2.2: 1, -0.5: 1, 2.3: 1, 6.2: 1, -
             6.3: 1, 9.2: 1, 1.5: 1, -4.5: 1, 0.6: 1, -9.9: 1, 8.8: 1, -7.0: 1, -6.0: 1, -5.0: 1, 4.5: 1, -3.0: 1, -1.0: 1, 6.5: 1}

    alpha = Puzzle2([], [], [], 0, 5)
    beta = Puzzle2([], [], [], 0, 5)

    alpha.initialize(a)
    beta.initialize(a)

    crosses = alpha.crossover(beta)

    alpha.mutate(a, adict)
    beta.mutate(a, adict)

    print alpha
    print alpha.fitness(adict, None)
    gud = alpha.getCopy()
    print gud
    print gud.fitness(adict, None)
    print gud.checkLegality(adict)
    gud.bin1[0] = -9.9
    gud.bin1[1] = -9.9
    gud.bin1[2] = -9.9
    gud.bin1[3] = -9.9
    (isValid, exportList, importList) = gud.checkLegality(adict)
    print isValid, exportList, importList
    print gud, "\n"
    gud.fixChildGivenLists(exportList, importList)
    print gud
    print gud.checkLegality(adict)
