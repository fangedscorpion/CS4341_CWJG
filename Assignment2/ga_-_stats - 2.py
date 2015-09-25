from ListParser import ListParser
from GenAlg import geneticAlgorithm

if __name__ == "__main__":
    debug_mode = 0

    runTimeSeconds = 10

    numberOfRuns = 5
    mutatePerc = 10

    startPopSize = 75

    geneticsType = 0  # 1 for elitism? 2 for culling?

    filename1 = "our_Puzzle"
    filename2 = "_sample.txt"

    puzzleNumList = [1, 2, 3]  # Add in 2 or 3 for more puzzles

    for puzzleNum in puzzleNumList:
        print puzzleNum
        for geneticsType in range(0, 3):
            print geneticsType
            the_list_parser = ListParser(
                open(filename1 + str(puzzleNum) + filename2, "r"), puzzleNum)
            fileWrite = open("genTest_-_Puzzle" + str(puzzleNum) + " type-" + str(geneticsType) + ".csv", "w+")
            fileWrite.write("low,high,median,generation\n")

            for j in range(0, numberOfRuns):
                print "sample: ", j
                (low, high, median) = geneticAlgorithm(puzzleNum, the_list_parser.getList(), runTimeSeconds, the_list_parser.getDictionary(
                ), pop_size, mutatePerc, the_list_parser.getTarget(), geneticsType)

                for k in range(0, len(low)):
                    fileWrite.write(str(low[k]) + "," + str(high[k]) + "," + str(median[k]) + "," + str(k*100) + "\n")
            fileWrite.close()
