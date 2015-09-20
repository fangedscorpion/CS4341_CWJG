from Chromosome import *
import random as rand
from Illegal import Illegal
from Location import Location
import copy


class Puzzle2(Chromosome):

    def __init__(self, bin1List, bin2List, bin3List, generation):
        super(Puzzle2, self).__init__(generation)
        self.bin1 = bin1List
        self.bin2 = bin2List
        self.bin3 = bin3List

        self.mutationThreshold = 50  # Percentage of 100 for each digit

    # This method initializes the Puzzle for generation 0
    # master is a list of all possible floats to create a Puzzle2 from
    def initialize(self, master):
        super(Puzzle2, self).__init__(0)
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

        # reset values in new dict to 0
        # thisDict = self.dictReset(thisDict)

        # form new dict
        # thisDict = self.countInDict(thisDict)

        # if master == thisDict:
        #     return True

        childDict = self.countInDict({})
        print childDict

        immigrationList = []
        deportationList = []
        childDictCopy = childDict.copy()

        for x in master.keys():
            if(childDictCopy.has_key(x)):
                if(not (childDictCopy[x][0] == master[x])):

                    diffCount = abs(master[x] - childDictCopy[x][0])
                    print "Key: ", x, " Diff count: ", diffCount
                    for ind in range(0, diffCount):
                        randInd = rand.randint(0, len(childDictCopy[x][1]) - 1)
                        print randInd, len(childDictCopy[x][1]) - 1
                        deportationList.append(
                            Illegal(x, diffCount, childDictCopy[x][1][randInd]))
            else:
                print "Key: ", x
                immigrationList.append(Illegal(x, 0, []))

        # These lists should be the same size
        return (len(deportationList) == 0 and len(immigrationList) == 0, deportationList, immigrationList)

    # This function forms a counting dictionary from the values in a Puzzle2
    # If a value in a Puzzle2 is not a key in the dictionary,
    # the unknown value is printed AND added to the list
    # INPUT -> (dict) empty dict
    # OUTPUT -> (dict) counted dict
    def countInDict(self, starting):
        print "%" * 20
        for i in range(0, len(self.bin1)):
            if (starting.has_key(self.bin1[i])):
                # print starting[self.bin1[i]][1]
                # print starting[self.bin1[i]][2] + [Location(1, i)]
                starting[self.bin1[i]] = (
                    starting[self.bin1[i]][1] + 1, starting[self.bin1[i]][2] + [Location(1, i)])
            else:
                # print "Bin 1 can't find key", self.bin1[i]
                starting[self.bin1[i]] = (1, [Location(1, i)])
                print "can't find key", self.bin1[i]
            if (starting.has_key(self.bin2[i])):
                # print starting[self.bin2[i]][0] + 1
                # print (1, list(starting[self.bin2[i]][1] + [Location(2, i)]))
                starting[self.bin2[i]] = (
                    starting[self.bin2[i]][0] + 1, list(starting[self.bin2[i]][1] + [Location(2, i)]))
            else:
                # print "Bin 2 can't find key", self.bin2[i]
                starting[self.bin2[i]] = (1, [Location(2, i)])

            if (starting.has_key(self.bin3[i])):
                starting[self.bin3[i]] = (
                    starting[self.bin3[i]][1] + 1, starting[self.bin3[i]][2] + [Location(3, i)])
            else:
                # print "Bin 3 can't find key", self.bin3[i]
                starting[self.bin3[i]] = (1, [Location(3, i)])

        return starting

    # This fixChild method makes a valid Puzzle2 chromosome from
    # an incorrect one and two lists of values that need to be swapped
    # One list is the values that need to be added into the object
    # The other list has the values that need to be moved out of the object
    def fixChild(self, exportList, importList):
        assert len(importList) == len(exportList)
        print importList
        print exportList

        for x in range(0, len(importList)):
            randint = rand.randint(0, len(importList) - 1)
            randint2 = rand.randint(0, len(exportList) - 1)

            importedIllegalObj = importList[randint]
            exportedIllegalObjLoc = exportList[randint2].getLocations()

            if(exportedIllegalObjLoc.getBin() == 1):
                # Location is in bin 1
                self.bin1[
                    exportedIllegalObjLoc.getIndex()] = importedIllegalObj.getValue()
                del importList[randint]
                del exportList[randint2]
            elif(exportedIllegalObjLoc.getBin() == 2):
                # Bin 2
                self.bin2[
                    exportedIllegalObjLoc.getIndex()] = importedIllegalObj.getValue()
                del importList[randint]
                del exportList[randint2]
            elif(exportedIllegalObjLoc.getBin() == 3):
                # Bin 3
                self.bin3[
                    exportedIllegalObjLoc.getIndex()] = importedIllegalObj.getValue()
                del importList[randint]
                del exportList[randint2]

        assert len(importList) == 0
        assert len(exportList) == 0

    # This function forms a counting dictionary from the values in a Puzzle2
    # If a value in a Puzzle2 is not a key in the dictionary, the unknown value is printed
    # INPUT -> (dict) starting dict
    # OUTPUT -> (dict) counted dict
    # def countInDict(self, starting):
    #     for i in range(0, len(self.bin1)):
    #         if (starting.has_key(self.bin1[i])):
    #             starting[self.bin1[i]] += 1
    #         else:
    #             print "can't find key", self.bin1[i]

    #         if (starting.has_key(self.bin2[i])):
    #             starting[self.bin2[i]] += 1
    #         else:
    #             print "can't find key", self.bin2[i]

    #         if (starting.has_key(self.bin3[i])):
    #             starting[self.bin3[i]] += 1
    #         else:
    #             print "can't find key", self.bin3[i]

    #     return starting

    # this function resets a dictonary, keeping the keys but resetting all values to 0
    # INPUT -> (dict)
    # OUTPUT -> (dict)
    def dictReset(self, dict):
        keys = dict.keys()
        for j in range(0, len(keys)):
            dict[keys[j]] = 0

        return dict

    # This method does a crossover for multiple Puzzles
    def crossover(self, other):
        cutPointInt = rand.randint(1, (len(self.bin1) - 1))
        print "Cut point: ", cutPointInt

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

        par1Bin1Front.extend(par2Bin1End)
        self.bin1 = par1Bin1Front
        par1Bin2Front.extend(par2Bin2End)
        self.bin2 = par1Bin2Front
        par1Bin3Front.extend(par2Bin3End)
        self.bin3 = par1Bin3Front

        par2Bin1Front.extend(par1Bin1End)
        other.bin1 = par2Bin1Front
        par2Bin2Front.extend(par1Bin2End)
        other.bin2 = par2Bin2Front
        par2Bin3Front.extend(par1Bin3End)
        other.bin3 = par2Bin3Front

    # this function evaluates the fitness of a Puzzle
    # fitness = product(bin1) + sum(bin2)
    def fitness(self):
        bProd = 1
        bSum = 0

        # because  for a Puzzle2 to be legal, all bins must be the same size
        # therefore, 1 for loop can be used
        for j in range(0, len(self.bin1)):
            bProd *= self.bin1[j]
            bSum += self.bin2[j]

        return (bProd + bSum) / 2

    # This is the version for when the chromosome is already legal
    def fixChildAfterMutate(self, listOfChangedNums):
        print listOfChangedNums

        for x in range(0, (len(listOfChangedNums) - 1), 2):
            # Generate another rand int in size of changed list
            ind1 = rand.randint(0, (len(listOfChangedNums) - 1))
            ind2 = rand.randint(0, (len(listOfChangedNums) - 1))
            while(ind2 == ind1):
                ind2 = rand.randint(0, (len(listOfChangedNums) - 1))
            print ind1, ind2

            changedTuple1 = listOfChangedNums[ind1]
            changedTuple2 = listOfChangedNums[ind2]

            # Swap values
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

    def getValidMutatedNumberIndex(self, lenMasterListOfNum):
        return rand.randint(0, (lenMasterListOfNum - 1))

    # this funcction mutates a Puzzle
    # It goes through all three at once and mutates if the number is between 1 and 8
    # If so it gets added to spareNums as a tuple with the changed index and the bin #
    # The fixChild class then makes the kid legal
    def mutate(self, masterListOfNum):
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

        self.fixChildAfterMutate(spareNums)

    def getBin1(self):
        return self.bin1

    def getBin2(self):
        return self.bin2

    def getBin2(self):
        return self.bin3

    def __repr__(self):
        return ("Bin1: " + str(self.bin1) + "\nBin2: " +
                str(self.bin2) + "\nBin3: " + str(self.bin3) + "\n")

if __name__ == '__main__':
    # from Puzzle2 import Puzzle2
    # a = [1, 0, -6, -9.9, 8, 4.5, 3, 3.8, 2.5]
    # master = {1: 1, 0: 1, -6: 1, -9.9: 1, 8: 1, 4.5: 1, 3: 1, 3.8: 1, 2.5: 1}
    # par1 = Puzzle2(a[0:3], a[3:6], a[6:9], 0)
    # par2 = Puzzle2(a[3:6], a[0:3], a[6:9], 0)
    # par3 = Puzzle2(a[6:9], a[3:6], a[0:3], 0)
    # par4 = Puzzle2(a[6:9], a[0:3], a[3:6], 0)

    # print par1
    # print par2
    # print par3
    # print par4

    # par4.mutate(a)  # Must pass in master list

    # print par4

    # print "Generation 0?: ", par1.getGeneration()

    # print "Fitness for par1: ", par1.fitness(), "\n"
    # print "-" * 20
    # print a

    # par5 = par2

    # print "Par1 before Xover:\n", par1
    # print "Par5 before Xover:\n", par5

    # par1.crossover(par5)

    # print "Par1 after Xover:\n", par1
    # print "Part after Xover:\n", par5

    # print master
    # print "Is legal: \n", par1.checkLegality(master)
    # par2.bin1[0] = 1

    # print "Is legal: \n", par2.checkLegality(master)

    # (legalHuh, exportL, importL) = par2.checkLegality(master)

    # par2.fixChild(exportL, importL)

    # print "Is legal: \n", par2.checkLegality(master)

    # print "Is legal: ", par2.checkLegality(master)
    # par5 = Puzzle2([], [], [], 2)
    # par5.initialize(a)
    # print par5
    # print par5.generation

    def testPrintAll():
        print "alpha: "
        print alpha
        print

        print "beta: "
        print beta
        print

        print "gamma: "
        print gamma
        print

        print "delta: "
        print delta
        print

    # a = [1, 0, -6, -9.9, 8, 4.5, 3, 3.8, 2.5]
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    alpha = Puzzle2([], [], [], 0)
    beta = Puzzle2([], [], [], 0)

    alpha.initialize(a)
    beta.initialize(a)

    alpha.crossover(beta)

    alpha.mutate(a)
    beta.mutate(a)

    print alpha
    print alpha.fitness()