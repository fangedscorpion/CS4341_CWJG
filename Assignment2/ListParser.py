from Piece import Piece

class ListParser(object):
    # file is the input list file
    # MakeList parses the input file and creates a list of numbers or pieces
    # puzzleNum is the puzzle type
    def __init__(self, file, puzzleNum):
        self.file = file
        (self.list, self.dictionary, self.target) = self.MakeList(self.file, puzzleNum)

    def updateDictionary(self, diction, key):
        if(diction.has_key(key)):
            diction[key] = diction.get(key) + 1
        else:
            diction[key] = 1

        return diction

    def getList(self):
        return self.list

    def getTarget(self):
        return self.target

    def getDictionary(self):
        return self.dictionary

    # parses the input file and creates the list
    # INPUT -> (file) input list
    # OUTPUT -> (list of num or Pieces and dictionary of items in the list)
    def MakeList(self, file, puzzleNum):
        # get all lines from input file
        lines = file.readlines()

        # split all idv input lines into lists
        for j in range(0, len(lines)):
            lines[j] = lines[j].split()

        if(puzzleNum == 1):
            startList = [None] * (len(lines)-1)
            dictionary = {};
        elif(puzzleNum == 2):
            startList = [None] * (len(lines))
            startList[0] = float(lines[0][0])
            dictionary = {(startList[0]): 1};
        elif(puzzleNum == 3):
            startList = [None] * (len(lines))
            startList[0] = Piece(lines[0][0], int(lines[0][1]), int(lines[0][2]), int(lines[0][3]))
            dictionary = {startList[0].getDictKey(): 1};

        print "Num of lines: ", len(lines)
        # assign values from lines into starting list
        for k in range(1, len(lines)):
            if(puzzleNum == 1):
                if(k == len(lines) - 1):
                    startList[k-1] = int(lines[k][0])   
                    dictionary = self.updateDictionary(dictionary, (lines[k][0]))
                    break

                startList[k-1] = int(lines[k][0])   
                dictionary = self.updateDictionary(dictionary, (lines[k][0]))

            elif(puzzleNum == 2):
                startList[k] = float(lines[k][0]) 
                dictionary = self.updateDictionary(dictionary, (lines[k][0]))
            elif(puzzleNum == 3):
                startList[k] = Piece(lines[k][0], int(lines[k][1]), int(lines[k][2]), int(lines[k][3]))
                dictionary = self.updateDictionary(dictionary, startList[k].getDictKey())

        # Return a tuple of all important info
        if(puzzleNum == 1):
            return (startList, dictionary, int(lines[0][0]))
        elif(puzzleNum == 2):
            return (startList, dictionary, None)
        elif(puzzleNum == 3):
            return (startList, dictionary, None)

if __name__ == "__main__":
    start_list = ListParser(open("sample_puzzle1_list.txt", "r"), 1)
    print start_list.getList()
    print 
    print start_list.getDictionary()
    print 
    print start_list.getTarget()

    start_list = ListParser(open("sample_puzzle2_list.txt", "r"), 2)
    print start_list.getList()
    print 
    print start_list.getDictionary()

    start_list = ListParser(open("piecelist.txt", "r"), 3)
    print start_list.getList()
    print 
    print start_list.getDictionary()