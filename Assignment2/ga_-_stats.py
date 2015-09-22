from ListParser import ListParser
from GenAlg import geneticAlgorithm

if __name__ == "__main__":
    debug_mode = 0
    run_time = 15
    puzzleNum = 2
    sample_size = 10
    filename1 = "sample_puzzle"
    filename2 = "_list.txt"



    for puzzleNum in range(1, 4):
        fileWrite = open("popTest_-_Puzzle" + str(puzzleNum) + ".csv", "w+")
        the_list_parser = ListParser(open(filename1 + str(puzzleNum) + filename2, "r"), puzzleNum)

        for pop_size in range(2, 8, 2):
            fileWrite.write(str(pop_size) + ",")
            for j in range(0, sample_size):
                # best = geneticAlgorithm(puzzleNum, the_list_parser.getList(), run_time, the_list_parser.getDictionary(), pop_size)
                # fileWrite.write(str(best.fitness()))
                fileWrite.write("3,") # swap with above when geneticAlgorithm is repaired

            fileWrite.write("\n")
        fileWrite.close()
