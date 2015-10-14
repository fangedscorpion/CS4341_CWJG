from Move import Move
from RolloutKey import RolloutKey


class BJGetter(object):
    DEBUG = 0

    def __init__(self, fileName):
        self.fileName = fileName

        # This dictionary is stored by the RolloutKey
        # Then the value is a tuple that is WINS then LOSES
        self.dictionary = {}

    # Updates the dictionary given the winning data
    def updateDictEntry(self, keyVal, didBust, wonData):
        wonData = int(wonData)

        if(self.dictionary.has_key(keyVal)):
            prevEntry = self.dictionary.get(keyVal)
            
            if(BJGetter.DEBUG == 1):
                print prevEntry

            if(wonData >= Move.WON_HAND_1):
                self.dictionary[keyVal] = (
                    prevEntry[0] + 1, prevEntry[1], prevEntry[2])
            elif(wonData == Move.LOST):
                self.dictionary[keyVal] = (
                    prevEntry[0], prevEntry[1] + 1, prevEntry[2])
            elif(wonData == Move.NOTCOMPLETE):
                if(didBust == 1):
                    self.dictionary[keyVal] = (
                        prevEntry[0], prevEntry[1] + 1, prevEntry[2])
                else:
                    self.dictionary[keyVal] = (
                        prevEntry[0], prevEntry[1], prevEntry[2] + 1)
        else:
            if(wonData >= Move.WON_HAND_1):
                self.dictionary[keyVal] = (1, 0, 0)
            elif(wonData == Move.LOST):
                self.dictionary[keyVal] = (0, 1, 0)
            elif(wonData == Move.NOTCOMPLETE):
                if(didBust == 1):
                    self.dictionary[keyVal] = (0, 1, 0)
                else:
                    self.dictionary[keyVal] = (0, 0, 1)
            
    def getDictionary(self):
        return self.dictionary

    # Returns a tuple of the percentage a particular dictionary key
    # Won against the visible diealer face card
    def getProbWinLost(self, keyVal):
        wins = self.dictionary[keyVal][0]
        losses = self.dictionary[keyVal][1]
        incomplete = self.dictionary[keyVal][2]

        totalPlayed = float(wins + losses)
        return (wins / totalPlayed, losses / totalPlayed)

    def getMoveLetter(self, moveName):
        if(str(moveName).lower() == Move.STAY.lower() or str(moveName).lower() == Move.STAY_SHORT.lower()):
            return Move.STAY_SHORT
        elif(str(moveName).lower() == Move.SPLIT.lower() or str(moveName).lower() == Move.SPLIT_SHORT.lower()):
            return Move.SPLIT_SHORT
        elif(str(moveName).lower() == Move.HIT.lower() or str(moveName).lower() == Move.HIT_SHORT.lower()):
            return Move.HIT_SHORT
        elif(str(moveName).lower() == Move.DOUBLE.lower() or str(moveName).lower() == Move.DOUBLE_SHORT.lower()):
            return Move.DOUBLE_SHORT

    def parseTheFile(self):
        fileHandleCurrent = open(self.fileName, "r")

        lines = fileHandleCurrent.readlines()

        i = 0
        while i < len(lines):
            line = lines[i].rstrip()
            line = line.split(",")
            if(BJGetter.DEBUG == 1):
                print line

            if(int(line[3]) == int(Move.SPLITNUM)):
                if(BJGetter.DEBUG == 1):
                    print "*"*50
                keyRollOut = RolloutKey(line[0], Move.SPLIT_SHORT, line[4])
                if(BJGetter.DEBUG == 1):
                    print keyRollOut
                self.updateDictEntry(keyRollOut, int(line[2]), line[5])
                if(BJGetter.DEBUG == 1):
                    print "BEFORE SPLIT", line
                
                i += 1
                line = lines[i].rstrip()
                line = line.split(",")
                if(BJGetter.DEBUG == 1):
                    print "First line of a split: ", line 
                tmpMove = None
                tmpMove2 = None
                while (not int(line[3]) == Move.NOTSPLIT and not int(line[3]) == Move.SPLITNUM):
                    keyRollOut = RolloutKey(
                        line[0], self.getMoveLetter(line[1]), line[4])
                    if(BJGetter.DEBUG == 1):                        
                        print "SPLIT: ", keyRollOut

                    if(int(line[3]) == 1 and (str(line[1]).lower() == Move.STAY.lower() or str(line[1]).lower() == Move.STAY_SHORT.lower())):
                        tmpMove = (keyRollOut, int(line[2]))
                        if(BJGetter.DEBUG == 1):
                            print "MV1: ", tmpMove
                    elif(int(line[3]) == 2 and (str(line[1]).lower() == Move.STAY.lower() or str(line[1]).lower() == Move.STAY_SHORT.lower())):
                        tmpMove2 = (keyRollOut, int(line[2]), int(line[5]))
                        if(BJGetter.DEBUG == 1):
                            print "MV2: ", tmpMove2
                    else:
                        self.updateDictEntry(keyRollOut, int(line[2]), int(line[5]))

                    i += 1
                    if(i < len(lines)):
                        line = lines[i].rstrip()
                        line = line.split(",")
                    else:
                        break
                    if(BJGetter.DEBUG == 1):
                        print line

                if(tmpMove2[2] == Move.WON_BOTH):
                    self.updateDictEntry(tmpMove[0], tmpMove[1], Move.WON_BOTH)
                    self.updateDictEntry(tmpMove2[0], tmpMove2[1], Move.WON_BOTH)
                elif(tmpMove2[2] == Move.WON_HAND_1):
                    self.updateDictEntry(tmpMove[0], tmpMove[1], Move.WON_HAND_1)
                    self.updateDictEntry(tmpMove2[0], tmpMove2[1], Move.LOST)
                elif(tmpMove2[2] == Move.WON_HAND_2):
                    self.updateDictEntry(tmpMove[0], tmpMove[1], Move.LOST)
                    self.updateDictEntry(tmpMove2[0], tmpMove2[1], Move.WON_HAND_2)
                else:
                    self.updateDictEntry(tmpMove[0], tmpMove[1], Move.LOST)
                    self.updateDictEntry(tmpMove2[0], tmpMove2[1], Move.LOST)

                if(BJGetter.DEBUG == 1):
                    print "END OF SPLIT"

                if(len(line) < 6):
                    fileHandleCurrent.close()
                    return

                if(i >= len(lines)):
                    fileHandleCurrent.close()
                    return

            if(str(line[1]).lower() == Move.SPLIT.lower() or str(line[1]).lower() == Move.SPLIT_SHORT.lower()):
                keyRollOut = RolloutKey(line[0], Move.SPLIT_SHORT, line[4])
                self.updateDictEntry(keyRollOut, int(line[2]), line[5])

            elif(str(line[1]).lower() == Move.STAY.lower() or str(line[1]).lower() == Move.STAY_SHORT.lower()):
                keyRollOut = RolloutKey(line[0], Move.STAY_SHORT, line[4])
                self.updateDictEntry(keyRollOut, int(line[2]), line[5])

            elif(str(line[1]).lower() == Move.HIT.lower() or str(line[1]).lower() == Move.HIT_SHORT.lower()):
                keyRollOut = RolloutKey(line[0], Move.HIT_SHORT, line[4])
                self.updateDictEntry(keyRollOut, int(line[2]), line[5])

            elif(str(line[1]).lower() == Move.DOUBLE.lower() or str(line[1]).lower() == Move.DOUBLE_SHORT.lower()):
                keyRollOut = RolloutKey(line[0], Move.DOUBLE_SHORT, line[4])
                self.updateDictEntry(keyRollOut, int(line[2]), line[5])

            i += 1

        fileHandleCurrent.close()

if __name__ == '__main__':
    from BJGetter import BJGetter
    import pickle
    import time

    print time.ctime()

    parserObj = BJGetter("BJstats_302.txt")

    parserObj.parseTheFile()

    pickle.dump(parserObj.getDictionary(), open("dict.p", "wb"))

    print "*" * 50

    #print parserObj.getDictionary()
    print time.ctime()
