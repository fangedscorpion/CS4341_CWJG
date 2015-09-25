import random
import time
from Chromosome import Chromosome
from Chromosome1 import Chromosome1
from Puzzle2 import Puzzle2
from Puzzle3 import Puzzle3
import copy
from Piece import Piece


def geneticAlgorithm(puzzle, validValues, allowedTime, masterDict, paramPopSize, mutationPerc, Puz1Target, mateMode):
    popSize = paramPopSize

    start = time.time()

    chromosomes = makeChromes(
        puzzle, validValues, masterDict, popSize, mutationPerc)

    gen = makeNodes(chromosomes)
    overallChampion = bestChrome(gen, masterDict).getCopy()
    overallChampion.fixChild(masterDict)
    # print overallChampion

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

    # print "Total Generations: " + str(generationNumber)

    return (overallChampion, generationNumber)


# creates 500 chromosomes (hopefully unique, though not explicitly)
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


def evalGen(gen, masterDict, Puz1Target):
    netFitness = 0
    netPercent = 0
    for node1 in gen:
        node1.fitness = node1.chromosome.fitness(masterDict, Puz1Target)
        netFitness += node1.fitness

    # print netFitness
    for node in gen:

        if(netFitness == 0):
            return
        percentFitness = (node.fitness / netFitness) * 100
        netPercent += percentFitness
        node.percentBound = netPercent


# make the new generation, new Gen is not mutated or valid
def mate(gen, popSize, mateMode, numSpecialNodes, masterDict, Puz1Target):
    iterations = len(gen)
    sorted(gen, key=lambda node: node.percentBound)
    preGen = []

    if mateMode == 1:  # if elite
        iterations -= numSpecialNodes
        for i in range(numSpecialNodes):
            preGen.append(gen[i])
    elif mateMode == 2:  # if culling
        for i in range(numSpecialNodes):
            gen[iterations - i - 1].fitness = 0
        evalGen(gen, masterDict, Puz1Target)
        sorted(gen, key=lambda node: node.percentBound)
    elif mateMode != 0:
        print "invalid mateMode, must be 0, 1, or 2"
        exit()

    for i in range(iterations / 2):
        foundA = 0
        foundB = 0
        point1 = random.random() * 100
        point2 = random.random() * 100
        # for each in gen:
        # print each.percentBound

        for j in range(1, len(gen)):
            if not foundA:
                if (point1 > gen[j - 1].percentBound):
                    parentA = gen[j]
                    foundA = 1
                elif (point1 < gen[0].percentBound):
                    parentA = gen[0]
                    foundA = 1

            if not foundB:
                if (point2 > gen[j - 1].percentBound):
                    parentB = gen[j]
                    foundB = 1
                elif (point2 < gen[0].percentBound):
                    parentB = gen[0]
                    foundB = 1

        # while (parentA is parentB): # if parents A and B are the same rerun B, no clones
        #     point2 = random.random()*100
        #     if (point2 > gen[j-1].percentBound) and (point2 < gen[j].percentBound):
        #         parentB = gen[j]

        children = parentA.chromosome.crossover(parentB.chromosome)
        child1 = node(children[0], 0, 0)
        child2 = node(children[1], 0, 0)
        preGen.append(child1)
        preGen.append(child2)

    return preGen


def mutateGen(gen, masterList, masterDict):
    mutGen = []
    for node in gen:
        node.chromosome.mutate(masterList, masterDict)


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

    testPuzzle1Values = [1, 2, 3, 4, 5]
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
    aPieceList = [d1, w1, w2, d2, w3, l1, l2]  # Best I think is score of 20
    aPieceDict = {d1.getDictKey(): 1, w1.getDictKey(): 1, w2.getDictKey(
    ): 1, d2.getDictKey(): 1, w3.getDictKey(): 1, l1.getDictKey(): 1, l2.getDictKey(): 1}

    testMateMode = 0
    mutatePerc = 10
    genSize = 50
    runTimeSecs = 3

    # puzzle, validValues, allowedTime, masterDict, paramPopSize, mutationPerc, Puz1Target, mateMode

    (best1, gens) = geneticAlgorithm(
        1, testPuzzle1Values, runTimeSecs, aPuzzle1Dict, genSize, mutatePerc, target, testMateMode)

    # (best2, gens) = geneticAlgorithm(
    # 2, aPuzzle2List, runTimeSecs, aPuzzle2Dict, genSize, mutatePerc, target,
    # testMateMode)

    # (best3, gens) = geneticAlgorithm(
    # 3, aPieceList, runTimeSecs, aPieceDict, genSize, mutatePerc, target,
    # testMateMode)

    print " "
    print "Puzzle 1 results:"
    print best1
    print best1.fitness(aPuzzle1Dict, target)
    # print " "
    # print "Puzzle 2 results:"
    # print best2
    # print best2.fitness(aPuzzle2Dict, target)
    # print " "
    # print "Puzzle 3 results:"
    # print best3
    # print best3.fitness(aPieceDict, target)
