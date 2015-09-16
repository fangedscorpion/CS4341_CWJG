class Puzzle1():
    
    def __init(self): #may need to pass it the entire list
        self.gen = [] #list of chromosomes

    #creates an entire first generation 
    def initFirstGen():
        pass

    #evaluates the generation
    def evalGen():
        pass

    #exchanges the latter part of each chromosome based on random indices
    #cut and splice method so the cut point can be different for each chromosome
    #returns a list of 2 new "children" chromosomes
    def crossover(chrom1, chrom2):
        #rand starts at 1 so there is always at least 1 element selected
        split1 = rand(1, len(chrom1.lon))
        split2 = rand(1, len(chrom2.lon))
        
        #children
        cchrom1 = chromosome1(chrom1.lon[0:split1] + chrom2.lon[split2:len(chrom2.lon)])
        cchrom2 = chromosome1(chrom2.lon[0:split2] + chrom1.lon[split1:len(chrom1.lon)])

        return [cchrom1, cchrom2]

    
