from Move import Move
from RolloutKey import RolloutKey

class BJGetter(object):

    def __init__(self, fileName):
        self.fileName = fileName

        # This dictionary is stored by the RolloutKey
        # Then the value is a tuple that is WINS then LOSES
        self.dictionary = {}

    # Updates the dictionary given the winning data
    def updateDictEntry(self, keyVal, wonData):
        wonData = int(wonData)

        if(self.dictionary.has_key(keyVal)):
            prevEntry = self.dictionary.get(keyVal)
            if(wonData == Move.WON):
                self.dictionary[keyVal] = (prevEntry[0]+1, prevEntry[1], prevEntry[2])
            elif(wonData == Move.LOST):
                self.dictionary[keyVal] = (prevEntry[0], prevEntry[1]+1, prevEntry[2])
            elif(wonData == Move.NOTCOMPLETE):
                self.dictionary[keyVal] = (prevEntry[0], prevEntry[1], prevEntry[2]+1)
        else:
            if(wonData == Move.WON):
                self.dictionary[keyVal] = (1, 0, 0)
            elif(wonData == Move.LOST):
                self.dictionary[keyVal] = (0, 1, 0)
            elif(wonData == Move.NOTCOMPLETE):
                self.dictionary[keyVal] = (0, 0, 1)

    def getDictionary(self):
        return self.dictionary

    #Returns a tuple of the percentage a particular dictionary key
    # Won against the visible diealer face card
    def getProbWinLost(self, keyVal):
        wins = self.dictionary[keyVal][0]
        losses = self.dictionary[keyVal][1]
        incomplete = self.dictionary[keyVal][2]

        totalPlayed = float(wins + losses)
        return (wins/totalPlayed, losses/totalPlayed)

    def getMoveLetter(self, moveName):
        if(str(moveName).lower() == Move.STAY.lower()):
            return Move.STAY_SHORT

        elif(str(moveName).lower() == Move.HIT.lower()):
            return Move.HIT_SHORT

        elif(str(moveName).lower() == Move.DOUBLE.lower()):
            return Move.DOUBLE_SHORT

    def parseTheFile(self):
        fileHandleCurrent = open(self.fileName, "r")

        lines = fileHandleCurrent.readlines()
       
        i = 0
        while i < len(lines):
            line = lines[i].rstrip()
            line = line.split(",")
            print line

            if(int(line[3]) == int(Move.SPLITNUM)):
                keyRollOut = RolloutKey(line[0], Move.SPLIT_SHORT, line[4], line[2], line[5])
                print keyRollOut
                self.updateDictEntry(keyRollOut, line[5])

                i += 1
                line = lines[i].rstrip()
                line = line.split(",")
                print line
                while (not int(line[3]) == Move.NOTSPLIT and not int(line[3]) == Move.SPLITNUM):

                    keyRollOut = RolloutKey(line[0], self.getMoveLetter(line[1]), line[4], line[2], line[5])
                    print keyRollOut
                    self.updateDictEntry(keyRollOut, line[5])
                    i += 1
                    print i
                    line = lines[i].rstrip()
                    line = line.split(",")
                    print line

            if(str(line[1]).lower() == Move.SPLIT.lower()):
                keyRollOut = RolloutKey(line[0], Move.SPLIT_SHORT, line[4], line[2], line[5])
                self.updateDictEntry(keyRollOut, line[5])

            elif(str(line[1]).lower() == Move.STAY.lower()):
                keyRollOut = RolloutKey(line[0], Move.STAY_SHORT, line[4], line[2], line[5])
                self.updateDictEntry(keyRollOut, line[5])

            elif(str(line[1]).lower() == Move.HIT.lower()):
                keyRollOut = RolloutKey(line[0], Move.HIT_SHORT, line[4], line[2], line[5])
                self.updateDictEntry(keyRollOut, line[5])

            elif(str(line[1]).lower() == Move.DOUBLE.lower()):
                keyRollOut = RolloutKey(line[0], Move.DOUBLE_SHORT, line[4], line[2], line[5])
                self.updateDictEntry(keyRollOut, line[5])

            i += 1

        fileHandleCurrent.close()

if __name__ == '__main__':
    from BJGetter import BJGetter

    parserObj = BJGetter("sample_BJ_data.txt")

    parserObj.parseTheFile()

    print "*"*50

    print parserObj.getDictionary()

    