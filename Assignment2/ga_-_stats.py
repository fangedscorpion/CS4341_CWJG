from ListParser import ListParser
from GenAlg import geneticAlgorithm

if __name__ == "__main__":
    debug_mode = 0

    runTimeSeconds = 3

    numberOfRuns = 3
    mutatePerc = 10
    
    startPopSize = 10
    popStepSize = 4
    endingPopSize = startPopSize + popStepSize

    geneticsType = 0 # 1 for elitism? 2 for culling?

    filename1 = "our_Puzzle"
    filename2 = "_sample.txt"

    puzzleNumList = [1] # Add in 2 or 3 for more puzzles

    for puzzleNum in puzzleNumList:

        print "puzzle: ", puzzleNum
        fileWrite = open("popTest_-_Puzzle" + str(puzzleNum) + ".csv", "w+")
        the_list_parser = ListParser(
            open(filename1 + str(puzzleNum) + filename2, "r"), puzzleNum)

        for pop_size in range(startPopSize, endingPopSize, popStepSize):
            print "\n"
            print "pop_size: ", pop_size
            fileWrite.write(str(pop_size) + ",")
            for j in range(0, numberOfRuns):
                print "-"*20
                print "sample: ", j
                (answer, gens) = geneticAlgorithm(puzzleNum, the_list_parser.getList(), runTimeSeconds, the_list_parser.getDictionary(
                ), pop_size, mutatePerc, the_list_parser.getTarget(), geneticsType)
                print answer, answer.fitness(the_list_parser.getDictionary(), the_list_parser.getTarget())
                fileWrite.write(str(answer.fitness(
                    the_list_parser.getDictionary(), the_list_parser.getTarget())) + ",")    
            fileWrite.write("\n")
        fileWrite.close()