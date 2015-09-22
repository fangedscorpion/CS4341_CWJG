from ListParser import ListParser
from GenAlg import geneticAlgorithm

if __name__ == "__main__":
    debug_mode = 0
    run_time = 15
    puzzleNum = 2
    sample_size = 10
    mutatePerc = 10
    filename1 = "ourPuzzle"
    filename2 = "_sample.txt"

    for puzzleNum in range(1, 4):
        print "puzzle: ", puzzleNum
        fileWrite = open("popTest_-_Puzzle" + str(puzzleNum) + ".csv", "w+")
        the_list_parser = ListParser(
            open(filename1 + str(puzzleNum) + filename2, "r"), puzzleNum)

        for pop_size in range(2, 100, 2):
            print "pop_size: ", pop_size
            fileWrite.write(str(pop_size) + ",")
            for j in range(0, sample_size):
                print "sample: ", j
                answer = geneticAlgorithm(puzzleNum, the_list_parser.getList(), run_time, the_list_parser.getDictionary(
                ), pop_size, mutatePerc, the_list_parser.getTarget(), 0)
                fileWrite.write(
                    str(answer.fitness(the_list_parser.getDictionary(), the_list_parser.getTarget())))

            fileWrite.write("\n")
        fileWrite.close()
