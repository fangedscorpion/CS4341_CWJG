import sys
from ListParser import ListParser
from geneticAlgo import geneticAlgo

if __name__ == "__main__":
    debug_mode = 1

    if len(sys.argv) != 4:
        print "Structure is: python ga.py filename.txt puzzleNum secondsToRun"
    else:
        filename = sys.argv[1]
        puzzleNum = int(sys.argv[2])
        secondsToRun = int(sys.argv[3])

        the_list_parser = ListParser(open(filename, "r"), puzzleNum)

        if(debug_mode == 1):
        	print the_list_parser.getList()
        	print
        	print the_list_parser.getDictionary()
        	print
        	print the_list_parser.getTarget()

        geneticAlgo(the_list_parser.getList(), secondsToRun, the_list_parser.getDictionary())


