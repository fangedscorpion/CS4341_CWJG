import random
import time
import Chromosome
from Puzzle2 import Puzzle2

def geneticAlgorithm(puzzle, validValues, allowedTime):
    popSize = 100
    start = time.time()
    chromosomes = makeChromes(puzzle, validValues, popSize)
    gen = makeNodes(chromosomes)
    masterDict = makeDict(validValues)

    while(time.time() < (start + allowedTime)):
        evalGen(gen)
        mate(gen)
        mutateGen(gen, validValues)

    return bestChrome(gen)



# creates 500 chromosomes (hopefully unique, though not explicitly)
def makeChromes(puzzle, validValues, popSize): 
    chromes = []
    for i in range(popSize):
        chromes.append(Puzzle2([], [], [], 0))
        chromes[i].initialize(validValues)

    return chromes

def makeNodes(chromosomes):
    nodes = []
    for i in range(len(chromosomes)):
        newNode = node(chromosomes[i], 0, 0)
        nodes.append(newNode)

    return nodes

def makeDict(values):
    newDict = {}
    for value in values:
        if newDict.has_key(value):
            newDict[value] += 1
        else:
            newDict[value] = 1

    return newDict

# defines the fitness of each node and the % of the net fitness which will be used for 
# mating
def evalGen(gen):
    netFitness = 0
    netPercent = 0
    for node in gen:
        node.fitness = node.chromosome.fitness()
        netFitness += node.fitness

    for node in gen:
        percentFitness = (node.fitness/netFitness)*100
        netPercent += percentFitness
        node.percentBound = netPercent




def mate(gen): #make the new generation, new Gen is not mutated or valid 
    preGen = []

    for i in range(len(gen)):
        preGen = []
        point1 = random.random()*100
        point2 = random.random()*100
        sorted(gen, key = lambda node: node.percentBound)
        for j in range(len(gen)):
            if (point1 > gen[j-1].percentBound) and (point1 < gen[j].percentBound):
                parentA = gen[j]
            if (point2 > gen[j-1].percentBound) and (point2 < gen[j].percentBound):
                parentB = gen[j]
        while (parentA is parentB): # if parents A and B are the same rerun B, no clones
            point2 = random.random()*100
            if (point2 > gen[j-1].percentBound) and (point2 < gen[j].percentBound):
                parentB = gen[j]

        children = parentA.chromosome.crossover(parentB.chromosome)
        child1 = node(children[0], 0, 0)
        child2 = node(children[1], 0, 0)
        preGen.append(child1)
        preGen.append(child2)

    gen = preGen

def mutateGen(gen, masterList):
    mutGen = []
    for node in gen:
        node.chromosome.mutate(masterList)

def bestChrome(gen):
    bestFitness = 0
    for node in gen:
        if node.fitness > bestFitness:
            bestFitness = node.fitness
            bestChrome = node.chromosome
    return bestChrome




class node():

    def __init__(self, chromosome, fitness, percentBound):
        self.chromosome = chromosome
        self.fitness = fitness
        self.percentBound = percentBound



if __name__ == "__main__":
    testValues = []

    for i in range(30):
        testValues.append(i+1)

    best = geneticAlgorithm(2, testValues, 10)













