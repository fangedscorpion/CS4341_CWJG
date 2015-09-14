import sys
from ListParser import ListParser

if __name__ == "__main__":
    debug_mode = 1

    if len(sys.argv) != 3:
        print "Structure is: python ga.py filename.txt puzzleNum secondsToRun"
    else:
        filename = sys.argv[1]
        puzzleNum = int(sys.argv[2])
        secondsToRun = int(sys.argv[3])

        the_list = ListParser(open(filename, "r"), puzzleNum)

        if(debug_mode == 1):
        	print the_list.getList()
        	print
        	print the_list.getDictionary()
        	print
        	print the_list.getTarget()