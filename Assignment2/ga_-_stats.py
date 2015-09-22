from ListParser import ListParser
from GenAlg import geneticAlgorithm

if __name__ == "__main__":
    debug_mode = 0
    run_time = 15
    puzzleNum = 2
    sample_size = 10
    filename = "sample_puzzle2_list.txt"
    fileWrite = open("popTest_-_Puzzle2.csv", "w+")

    the_list_parser = ListParser(open(filename, "r"), puzzleNum)

    if(debug_mode == 1):
        print the_list_parser.getList()
        print
        print the_list_parser.getDictionary()
        print
        print the_list_parser.getTarget()

    for pop_size in range(2, 8, 2):
        fileWrite.write(str(pop_size) + ",")
        for j in range(0, sample_size):
            # best = geneticAlgorithm(puzzleNum, the_list_parser.getList(), run_time, the_list_parser.getDictionary(), pop_size)
            # fileWrite.write(str(best.fitness()))
            fileWrite.write(str(j) + ",")

        fileWrite.write("\n")
    fileWrite.close()
