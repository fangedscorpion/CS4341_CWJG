import random

def geneticAlgorithm(puzzle, validValues):
    chromosomes = makeChromes(puzzle)
    gen = makeNodes(chromosomes)

    while(time ldakjflasdj):
        evalGen(gen)
        mate(gen)
        mutate(gen)
        makeValid(gen)


# creates 500 chromosomes (hopefully unique, though not explicitly)
def makeChromes(puzzle, validValues): 
    chromes = []
    for i in range(500):
        chromes[i] = Puzzle2([], [], [], 0)
        chromes[i].initialize(validValues)

    return chromes

def makeNodes(chromosomes):
    nodes = []
    for i in len(chromosomes):
        nodes[i] = node(chromosomes, 0, 0)

    return nodes

# 
def evalGen(gen):
    netFitness = 0
    netPercent = 0
    for node in len(gen):
        node.fitness = node.chromosome.fitness()
        netFitness += node.fitness

    for node in len(gen):
        percentFitness = (node.fitness/netFitness)*100
        netPercent += percentFitness
        node.percentBound = netPercent




def mate(gen): #make the new generation, new Gen is not mutated or valid 
    for i in len(gen):
        point1 = random.random()*100
        point2 = random.random()*100
        for j in len(gen):
            if (point1 > gen[j-1]) and (point1 < gen[j]):
                parentA = gen[j]
            if (point2 > gen[j-1]) and (point2 < gen[j]):
                parentB = gen[j]

        


    


class node():

    def __init__(self, chromosome, fitness, percentBound):
        self.chromosome = chromosome
        self.fitness = fitness
        self.percentBound = percentBound
















