import sys
from ListParser import ListParser
from GenAlg2 import geneticAlgorithm

if __name__ == "__main__":
    debug_mode = 0

    if len(sys.argv) < 4:
        print "Structure is: python ga.py filename.txt puzzleNum secondsToRun"
    else:
        filename = sys.argv[1]
        puzzleNum = int(sys.argv[2])
        secondsToRun = int(sys.argv[3])

        if (len(sys.argv) == 5):
            mode = int(sys.argv[4])
        else:
            mode = 0

        the_list_parser = ListParser(open(filename, "r"), puzzleNum)
        mutationRate = 10
        population = 500

        if(debug_mode == 1):
            print the_list_parser.getList()
            print
            print the_list_parser.getDictionary()
            print
            print the_list_parser.getTarget()

        answer = geneticAlgorithm(puzzleNum, the_list_parser.getList(), secondsToRun, the_list_parser.getDictionary(
        ), population, mutationRate, the_list_parser.getTarget(), mode)
        print "\nBest solution: \n", answer[0]
        print "\nScore:\n", answer[0].fitness(the_list_parser.getDictionary(), the_list_parser.getTarget())
        print "\nTotal generations: \n", answer[1]
