from ListParser import ListParser
from GenAlg import geneticAlgorithm

if __name__ == "__main__":
    debug_mode = 0

    runTimeSeconds = 5

    numberOfRuns = 3
    mutatePerc = 10

    startPopSize = 10
    popStepSize = 4
    endingPopSize = startPopSize + popStepSize

    geneticsType = 0  # 1 for elitism? 2 for culling?

    filename1 = "our_Puzzle"
    filename2 = "_sample.txt"
    j = 0

    puzzleNumList = [3]  # Add in 2 or 3 for more puzzles

    for puzzleNum in puzzleNumList:
        if (puzzleNum == 1) and (j == 0):
            the_list_parser = ListParser(
                open(filename1 + str(puzzleNum) + filename2, "r"), puzzleNum)
            j += 1
            fileWrite = open("popTest_-_Puzzle" + str(puzzleNum) + ".csv", "w+")
        elif (puzzleNum == 1) and (j == 1):
            the_list_parser = ListParser(
                open(filename1 + str(puzzleNum) + "-1" + filename2, "r"), puzzleNum)
            fileWrite = open("popTest_-_Puzzle" + str(puzzleNum) + "-1" + ".csv", "w+")
        else:
            the_list_parser = ListParser(
                open(filename1 + str(puzzleNum) + filename2, "r"), puzzleNum)
            fileWrite = open("popTest_-_Puzzle" + str(puzzleNum) + ".csv", "w+")

        print "puzzle: ", puzzleNum
        fileWrite = open("popTest_-_Puzzle" + str(puzzleNum) + ".csv", "w+")

        for pop_size in range(startPopSize, endingPopSize, popStepSize):
            print "\n"
            print "pop_size: ", pop_size
            fileWrite.write(str(pop_size) + ",")
            for j in range(0, numberOfRuns):
                print "-" * 20
                print "sample: ", j
                (answer, gens) = geneticAlgorithm(puzzleNum, the_list_parser.getList(), runTimeSeconds, the_list_parser.getDictionary(
                ), pop_size, mutatePerc, the_list_parser.getTarget(), geneticsType)
                print answer, answer.fitness(the_list_parser.getDictionary(), the_list_parser.getTarget())
                fileWrite.write(str(answer.fitness(
                    the_list_parser.getDictionary(), the_list_parser.getTarget())) + ",")
            fileWrite.write("\n")
        fileWrite.close()
