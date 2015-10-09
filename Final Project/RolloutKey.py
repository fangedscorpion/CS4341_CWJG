
class RolloutKey(object):

    def __init__(self, playerScore, moveName, dealerScore, bustedAfterMove, wonVsDealer):
        self.playerScore = playerScore
        self.dealerScore = dealerScore
        self.moveName = moveName

        #Probably don't need these last attributes
        self.bustedAfterMove = bustedAfterMove
        self.won = wonVsDealer

    def getPlayerScore(self):
        return self.playerScore

    def getDealerScore(self):
        return self.dealerScore

    def getMoveName(self):
        return self.moveName

    def getWon(self):
        return self.won

    def getIfBustedPostMove(self):
        return self.bustedAfterMove

    def __repr__(self):
        return ("p" + str(self.playerScore) + \
                "d" + str(self.dealerScore) + \
                "m" + str(self.moveName) + \
                "w" + str(self.won))

    def __eq__(self, other):
        return int(self.playerScore) == int(other.getPlayerScore()) and \
                int(self.dealerScore) == int(other.getDealerScore()) and \
                str(self.moveName).lower() == str(other.getMoveName()).lower()

if __name__ == '__main__':
    from RolloutKey import RolloutKey

    dictRollout = {}
    aKey1 = RolloutKey(10, "H", 17, 0, 0)
    aKey4 = RolloutKey(10, "H", 19, 0, 0)
    aKey2 = RolloutKey(10, "S", 20, 0, -1)
    aKey3 = RolloutKey(19, "S", 20, 0, 1)

    print not aKey1 == aKey2
    print aKey1, aKey2

    dictRollout[aKey1] = (1,0,0)
    dictRollout[aKey2] = (0,1,0)

    print dictRollout