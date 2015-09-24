from ListParser import ListParser
from GenAlg import geneticAlgorithm

if __name__ == "__main__":
    debug_mode = 0

    runTimeSeconds = 15

    numberOfRuns = 10
    mutatePerc = 10

    startPopSize = 10
    popStepSize = 2
    endingPopSize = 152

    geneticsType = 0  # 1 for elitism? 2 for culling?

    filename1 = "our_Puzzle"
    filename2 = "_sample.txt"

    puzzleNumList = [1, 2, 3]  # Add in 2 or 3 for more puzzles

    for puzzleNum in puzzleNumList:
        the_list_parser = ListParser(
            open(filename1 + str(puzzleNum) + filename2, "r"), puzzleNum)
        fileWrite = open("popTest_-_Puzzle" + str(puzzleNum) + ".csv", "w+")

        print "puzzle: ", puzzleNum
        fileWrite = open("popTest_-_Puzzle" + str(puzzleNum) + ".csv", "w+")

        for pop_size in range(startPopSize, endingPopSize, popStepSize):
            print "pop_size: ", pop_size
            for j in range(0, numberOfRuns):
                print "sample: ", j
                (answer, gens) = geneticAlgorithm(puzzleNum, the_list_parser.getList(), runTimeSeconds, the_list_parser.getDictionary(
                ), pop_size, mutatePerc, the_list_parser.getTarget(), geneticsType)
                fileWrite.write(str(pop_size) + "," + str(answer.fitness(
                    the_list_parser.getDictionary(), the_list_parser.getTarget())) + "," + str(answer.getGeneration()) + "," + str(gens) + "\n")
        fileWrite.close()

        if puzzleNum == 1:
            print "1 - hard"
            the_list_parser = ListParser(
                open(filename1 + str(puzzleNum) + "-1" + filename2, "r"), puzzleNum)
            fileWrite = open(
                "popTest_-_Puzzle" + str(puzzleNum) + "-1" + ".csv", "w+")

            for pop_size in range(startPopSize, endingPopSize, popStepSize):
                print "pop_size: ", pop_size
                for j in range(0, numberOfRuns):
                    print "sample: ", j
                    (answer, gens) = geneticAlgorithm(puzzleNum, the_list_parser.getList(), runTimeSeconds, the_list_parser.getDictionary(
                    ), pop_size, mutatePerc, the_list_parser.getTarget(), geneticsType)
                    fileWrite.write(str(pop_size) + "," + str(answer.fitness(
                        the_list_parser.getDictionary(), the_list_parser.getTarget())) + "," + str(answer.getGeneration()) + "," + str(gens) + "\n")
            fileWrite.close()

        if puzzleNum == 3:
            print "3 - long"
            runTimeSeconds = 60
            # numberOfRuns = 3
            the_list_parser = ListParser(
                open(filename1 + str(puzzleNum) + filename2, "r"), puzzleNum)
            fileWrite = open(
                "popTest_-_Puzzle" + str(puzzleNum) + "-1" + ".csv", "w+")

            for pop_size in range(startPopSize, endingPopSize, popStepSize):
                print "pop_size: ", pop_size
                for j in range(0, numberOfRuns):
                    print "sample: ", j
                    (answer, gens) = geneticAlgorithm(puzzleNum, the_list_parser.getList(), runTimeSeconds, the_list_parser.getDictionary(
                    ), pop_size, mutatePerc, the_list_parser.getTarget(), geneticsType)
                    fileWrite.write(str(pop_size) + "," + str(answer.fitness(
                        the_list_parser.getDictionary(), the_list_parser.getTarget())) + "," + str(answer.getGeneration()) + "," + str(gens) + "\n")
            fileWrite.close()
