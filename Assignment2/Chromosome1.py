import random
from Chromosome import Chromosome


class Chromosome1(Chromosome):

    def __init__(self, listOfNumbers, gen, probabilityMutate):
        # I guess this does not happen because of an initialize function...?
        self.lon = listOfNumbers
        # probability each gene in the chromosome gets mutated
        self.probMutate = probabilityMutate
        self.generation = gen

    # Initialize an instance of a chromosome based on the possible numbers
    # that can be added to self. Possible numbers comes from keys of master
    # (the master dictionary)
    def initialize(self, master):
        self.generation = 0
        added = 0
        if(len(master) == 0):
            print "Input master list of numbers must have at least one element!"
            exit(0)

        chromLen = random.randint(0, len(master))

        while(added < chromLen):
            addChoice = master[random.randint(0, len(master) - 1)]

            self.lon.append(addChoice)
            added += 1

    # get score from the list of numbers. Target is the number trying to be
    # reached
    def fitness(self, dict, target):
        sumList = sum(self.lon)
        self.target = target
        if (self.checkLegality(dict) and sumList <= target):
            return sumList
        else:  # sum exceeded target means fitness 0
            return 0

    # crossover this chromosome with the given chromosome
    def crossover(self, chrom):
        if(len(self.lon) > 1):
            split1 = random.randint(1, len(self.lon) - 1)
        else:
            split1 = 0
        if(len(chrom.lon) > 1):
            split2 = random.randint(1, len(chrom.lon) - 1)
        else:
            split2 = 0

        # children
        cchrom1 = Chromosome1(list(self.lon[
                              0:split1] + chrom.lon[split2:len(chrom.lon)]), (self.getGeneration() + 1), self.probMutate)
        cchrom2 = Chromosome1(list(chrom.lon[
                              0:split2] + self.lon[split1:len(self.lon)]), (chrom.getGeneration() + 1), self.probMutate)

        return (cchrom1, cchrom2)

    # mutate based on probability, if it mutates needs to take a list from the
    # "master" dictionary. If turns into just a list, remove .keys
    def mutate(self, masterList, masterDict):
        master = masterList

        # Have to truncate size to the master list size at most
        # if (len(self.lon) > len(masterList)):
        #     self.lon = list(self.lon[0:len(masterList) - 1])

        i = 0
        while i < len(self.lon):
            # If less than probMutate, mutate. Probabilities scaled for 0-100
            # to avoid floats. Because I can.
            if(random.randint(1, 100) < self.probMutate):
                mutationType = random.randint(1, 3)

                if(mutationType == 1):  # Transform
                    self.lon[i] = master[random.randint(0, len(master) - 1)]
                    i += 1
                elif(mutationType == 2):  # Remove number
                    del self.lon[i]
                else:  # Add number
                    self.lon.append(master[random.randint(0, len(master) - 1)])
                    i += 1
                # print "Mutated to", str(self.lon[i]), " at ", str(i)
            else:
                i += 1

        # print "Mutate before fix"
        # print self.lon

        self.fixChild(masterDict) # Python is reference based, so no need to
        # return it

    # specifically to check the validity of one number to see if it is a valid
    # mutation. MasterDict needs to be the dictionary
    def isValid(self, num1, masterDict):
        checkNum = masterDict[num1]
        if(self.lon.count(num1) > checkNum):
            return False
        else:
            return True

    # make it valid if need be
    def fixChild(self, masterDict):
        chromList = self.lon
        masterList = masterDict.keys()
        removeList = [] #indices to remove
        for i in range(len(chromList)):
            keep_going = not self.isValid(chromList[i], masterDict)

            #while(not self.isValid(chromList[i], masterDict)):
            while (keep_going): # shits going down with this number, yo
                if(len(chromList) > len(masterList)):
                    removeList.append(i)
		    keep_going = False
                else:
                    chromList[i] = random.choice(masterList)
                    keep_going = False
        for j in range(len(removeList) - 1, -1, -1):
            chromList.pop(j)

    def getGeneration(self):
        return self.generation

    def checkLegality(self, masterDict):
        total = 0
        for j in masterDict.keys():
            total += masterDict[j]

        if len(self.lon) > total:
            return False

        for digit in self.lon:
            if(not self.isValid(digit, masterDict)):
                return False

        return True

    def getCopy(self):
        copyChromeo = Chromosome1(
            list(self.lon), self.generation, self.probMutate)
        return copyChromeo

    def __repr__(self):
        return (str(self.lon) + " Gen: " + str(self.generation))


if __name__ == '__main__':
    masterDictionary = {1: 2, 2: 1, 3: 1, 4: 3, 5: 2, 6: 1,
                        7: 1, 8: 4, 9: 0, 10: 2, 11: 2, 12: 1, 13: 3, 14: 1, 15: 5}
    masterList = [1, 2, 1, 3, 4, 5, 4, 5, 4, 6, 7, 8, 8, 8, 8,
                  10, 10, 11, 11, 12, 13, 13, 13, 14, 15, 15, 15, 15, 15]
    chrom1 = Chromosome1([], 0, 0)
    chrom1.initialize(masterList)
    print "1", chrom1.lon
    chrom2 = Chromosome1([], 0, 0)
    chrom2.initialize(masterList)
    print "2", chrom2.lon
    result = chrom1.crossover(chrom2)
    print(result[0].lon)
    print(result[1].lon)
    print("MUTATE!!!")
    result[0].mutate(masterList)
    result[1].mutate(masterList)
    new1 = result[0]
    new2 = result[1]
    print (new1.lon)
    print (new2.lon)
