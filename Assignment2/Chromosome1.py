class chromosome1(Chromosome):
    
    def __init__(self, listOfNumbers):
        self.lon = listOfNumbers
        self.fitness = 0
        self.probMutate = 20
        

    #Initialize an instance of a chromosome based on the possible numbers that can be added to self.lon(master)
    def initialize(self, master):
        pass

    


    #get score from the list of numbers
    def fitness(self):
        return sum(self.lon)

    #crossover this chromosome with the given chromosome
    def crossover(chrom):
        #rand starts at 1 so there is always at least 1 element selected
        split1 = rand(1, len(self.lon))
        split2 = rand(1, len(chrom.lon))

        #children
        cchrom1 = chromosome1(self.lon[0:split1] + chrom.lon[split2:len(chrom.lon)])
        cchrom2 = chromosome1(chrom.lon[0:split2] + self.lon[split1:len(self.lon)])

        #So this is probably not what it returns
        return [cchrom1, cchrom2]


    #mutate based on probability, if it mutates needs to take a list from the "master" list of numbers, passed in here 
    def mutate(self, master):
        for i in range(0, self.lon): #iterate over each number in list
            if(rand(0, 100) > self.probMutate): #If greater than probMutate, mutate. Probabilities scaled for 0-100 to avoid floats
                self.lon[i] = master[rand(0, len(master)-1)]
                while(!isValid(self.lon[i], master))): #if it swapped to an invalid number, swap to a different one
                    self.lon[i] = master[rand(0, len(master)-1)]
                
                    
                
                
                
    #specifically to check the validity of one number to see if it is a valid mutation
    def isValid(num1, masterNum):
        

    #check validity
    def checkLegality(self):
        pass

    #make it valid if need be
    def fixChild(self):
        pass

