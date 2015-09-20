import random
class chromosome1():
    
    def __init__(self, listOfNumbers):
        self.lon = listOfNumbers #I guess this does not happen because of an initialize function...?
        self.dictionary = {} #empty dictionary fills initialization
        self.probMutate = 20 #probability each gene in the chromosome gets mutated
    #Initialize an instance of a chromosome based on the possible numbers that can be added to self. Possible numbers comes from keys of master (the master dictionary)
    def initialize(self, master):
        added = 0
        chromLen = random.randint(0, 25) #whatever we decide should be the max length of a chromosome 
        while(added <= chromLen):
            addChoice = random.choice(master.keys())
            if(self.lon.count(addChoice) < master[addChoice]): #if there are not too many of this number in the list...
                self.lon.append(addChoice)
                added += 1


    #get score from the list of numbers
    def fitness(self):
        return sum(self.lon)

    #crossover this chromosome with the given chromosome
    def crossover(self, chrom):
        split1 = random.randint(0, len(self.lon) - 1)
        split2 = random.randint(0, len(chrom.lon) - 1) 

        #children
        cchrom1 = chromosome1(self.lon[0:split1] + chrom.lon[split2:len(chrom.lon)])
        cchrom2 = chromosome1(chrom.lon[0:split2] + self.lon[split1:len(self.lon)])

        #So this is probably not what it returns
        return [cchrom1, cchrom2]


    #mutate based on probability, if it mutates needs to take a list from the "master" dictionary. If turns into just a list, remove .keys
    def mutate(self, masterDict):
        master = masterDict.keys() #remove this and set parameter to master if it is just a list
        for i in range(0, len(self.lon) - 1): #iterate over each number in list
            if(random.randint(0, 100) < self.probMutate): #If less than probMutate, mutate. Probabilities scaled for 0-100 to avoid floats. Because I can.
                self.lon[i] = master[random.randint(0, len(master)-1)]
                while(not isValid(self, self.lon[i], master)): #if it swapped to an invalid number, swap to a different one
                    self.lon[i] = master[random.randint(0, len(master)-1)]
        return self #not sure what this is returning
                
                
                
    #specifically to check the validity of one number to see if it is a valid mutation. MasterDict needs to be the dictionary
    def isValid(self, num1, masterDict):
        #mport pdb; pdb.set_trace()
        checkNum = masterDict[num1]
        if(self.lon.count(num1) > checkNum):
            return False
        else:
            return True
            

    #check validity
    def checkLegality(self):
        pass

    #make it valid if need be
    def fixChild(self):
        pass


if __name__ == '__main__':
    masterDictionary = {1:2, 2:1, 3:1, 4:3, 5:2, 6:1, 7:1, 8:4, 9:0, 10:2, 11:2, 12:1, 13:3, 14:1, 15:5}
    chrom1 = chromosome1([])
    chrom1.initialize(masterDictionary)
    print(chrom1.lon)
    chrom2 = chromosome1([])
    chrom2.initialize(masterDictionary)
    print(chrom2.lon)
    result = chrom1.crossover(chrom2)
    print(result[0].lon)
    print(result[1].lon)
    print("MUTATE!!!")
    new1 = result[0].mutate(masterDictionary)
    new2 = result[1].mutate(masterDictionary)
    print (new1.lon)
    print (new2.lon)
    












