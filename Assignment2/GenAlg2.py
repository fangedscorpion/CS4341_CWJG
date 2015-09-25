import random
import time
from Chromosome import Chromosome
from Chromosome1 import Chromosome1
from Puzzle2 import Puzzle2
from Puzzle3 import Puzzle3
import copy
from Piece import Piece

#Finds the best solution (that it can in the time limit) to the given puzzle 
def geneticAlgorithm(puzzle, validValues, allowedTime, masterDict, paramPopSize, mutationPerc, Puz1Target, mateMode):
    popSize = paramPopSize

    start = time.time()

    chromosomes = makeChromes(
        puzzle, validValues, masterDict, popSize, mutationPerc)

    gen = makeNodes(chromosomes)
    overallChampion = bestChrome(gen, masterDict).getCopy()
    overallChampion.fixChild(masterDict)

    generationNumber = 0
    while(time.time() < (start + allowedTime)):
        evalGen(gen, masterDict, Puz1Target)
        gen = mate(gen, popSize, mateMode, 8, masterDict, Puz1Target)
        mutateGen(gen, validValues, masterDict)
        daWinner = bestChrome(gen, masterDict).getCopy()

        if daWinner.fitness(masterDict, Puz1Target) > overallChampion.fitness(masterDict, Puz1Target):

            gud = daWinner.getCopy()
            overallChampion = gud

        generationNumber += 1

 

    return (overallChampion, generationNumber)


# creates x chromosomes (hopefully unique, though not explicitly)
def makeChromes(puzzle, validValues, masterDict, popSize, mutatePerc):
    chromes = []
    for i in range(popSize):
        if(puzzle == 1):
            chromes.append(Chromosome1([], 0, mutatePerc))
        elif(puzzle == 2):
            chromes.append(Puzzle2([], [], [], 0, mutatePerc))
        elif(puzzle == 3):
            chromes.append(Puzzle3(0, mutatePerc))

        chromes[i].initialize(validValues)
        chromes[i].fixChild(masterDict)
        

    return chromes

# makes a list of nodes from the chromosomes
def makeNodes(chromosomes):
    nodes = []
    for i in range(len(chromosomes)):
        newNode = node(chromosomes[i], 0, 0)
        nodes.append(newNode)

    return nodes


# defines the fitness of each node and the % of the net fitness which will be used for
# mating
def evalGen(gen, masterDict, Puz1Target):
    netFitness = 0
    netPercent = 0
    for node1 in gen:
        node1.fitness = node1.chromosome.fitness(masterDict, Puz1Target)
        netFitness += node1.fitness

    gen = sorted(gen, key=lambda node: node.fitness)

    for i in range(len(gen)):
        if(netFitness == 0):
            gen[i].percentBound = (float(i)*100/len(gen))

        else:
            percentFitness = (float(gen[i].fitness) / netFitness) * 100
            netPercent += percentFitness
            gen[i].percentBound = netPercent


# make the new generation, preGen is not mutated or valid
def mate(gen, popSize, mateMode, numSpecialNodes, masterDict, Puz1Target):
    iterations = len(gen)
    gen = sorted(gen, key=lambda node: node.percentBound)

    preGen = []

    if mateMode == 1:  # if elite
        iterations -= numSpecialNodes
        for i in range(numSpecialNodes):
            preGen.append(gen[i])
    elif mateMode == 2:  # if culling
        for i in range(numSpecialNodes):
            gen[iterations - i - 1].fitness = 0
        evalGen(gen, masterDict, Puz1Target)
        gen = sorted(gen, key=lambda node: node.percentBound)
    elif mateMode != 0: # if invalid mode number
        print "invalid mateMode, must be 0, 1, or 2"
        exit()

    for i in range(iterations / 2):
        foundA = 0
        foundB = 0
        point1 = 0
        point2 = 0
        while point1 == 0:
            point1 = random.random()*100
        while point2 == 0:
            point2 = random.random()*100

        for j in range(1, len(gen)):
            if not foundA:
                if point1 < gen[j].percentBound:
                    parentA = gen[j]
                    foundA = 1
                else:
                    parentA = gen[len(gen)-1]

            if not foundB:
                if point2 < gen[j].percentBound:
                    parentB = gen[j]
                    foundB = 1
                else:
                    parentB = gen[len(gen)-1]

        children = parentA.chromosome.crossover(parentB.chromosome)
        child1 = node(children[0], 0, 0)
        child2 = node(children[1], 0, 0)
        preGen.append(child1)
        preGen.append(child2)

    return preGen


# mutates all elements of the generation and makes them valid
def mutateGen(gen, masterList, masterDict):
    mutGen = []
    for node in gen:
        node.chromosome.mutate(masterList, masterDict)


# find the best chromosome in a list of chromosomes given the allowed variables (dict)
def bestChrome(gen, masterDict):
    if (len(gen) == 0):
        print "gen is empty"
        exit()

    best = gen[0].chromosome.getCopy()
    bestFitness = gen[0].fitness

    for node in gen:
        if (node.fitness > bestFitness):
            bestFitness = node.fitness
            best = node.chromosome.getCopy()

    return best


class node():

    def __init__(self, chromosome, fitness, percentBound):

        self.chromosome = chromosome
        self.fitness = fitness
        self.percentBound = percentBound

if __name__ == "__main__":

    aPuzzle1List = [1, 2, 3, 4, 5]
    aPuzzle1Dict = {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
    target = 10

    aPuzzle2List = [1, 0, -6, -9.9, 8, 4.5, 3, 3.8, 2.5]
    aPuzzle2Dict = {
        1: 1, 0: 1, -6: 1, -9.9: 1, 8: 1, 4.5: 1, 3: 1, 3.8: 1, 2.5: 1}

    d1 = Piece("Door", 5, 3, 2, 0)
    w1 = Piece("Wall", 5, 5, 1, 1)
    w2 = Piece("Wall", 4, 3, 1, 2)
    d2 = Piece("Door", 3, 5, 2, 3)
    w3 = Piece("Wall", 3, 3, 2, 4)
    l1 = Piece("Lookout", 2, 2, 3, 5)
    l2 = Piece("Lookout", 3, 1, 2, 6)
    aPieceList = [d1, w1, w2, d2, w3, l1, l2]  
    aPieceDict = {d1.getDictKey(): 1, w1.getDictKey(): 1, w2.getDictKey(
    ): 1, d2.getDictKey(): 1, w3.getDictKey(): 1, l1.getDictKey(): 1, l2.getDictKey(): 1}

    testMateMode = 0
    mutatePerc = 10
    genSize = 50
    runTimeSecs = 10

    # geneticAlgorithm inputs: (yeah theres a lot)
    # puzzle, validValues, allowedTime, masterDict, paramPopSize, mutationPerc, Puz1Target, mateMode

    # (sampleBest1, sampleBest1gen) = geneticAlgorithm(
    #     1, aPuzzle1List, runTimeSecs, aPuzzle1Dict, genSize, mutatePerc, target, testMateMode)

    # print sampleBest1.fitness(aPuzzle1Dict, target), sampleBest1

    # (sampleBest2, sampleBest2gen) = geneticAlgorithm(
    #     2, aPuzzle2List, runTimeSecs, aPuzzle2Dict, genSize, mutatePerc, target, testMateMode)

    # print sampleBest2.fitness(aPuzzle2Dict, target), sampleBest2

    (sampleBest3, sampleBest3gen) = geneticAlgorithm(
        3, aPieceList, runTimeSecs, aPieceDict, genSize, mutatePerc, target, testMateMode)

    print sampleBest3.fitness(aPieceDict, target), sampleBest3
    
