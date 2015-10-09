
class RolloutKey(object):

    def __init__(self, playerScore, moveName, dealerScore):
        self.playerScore = playerScore
        self.dealerScore = dealerScore
        self.moveName = moveName

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

    def __hash__(self):
        return hash((str(self)))

    def __repr__(self):
        return ("p" + str(self.playerScore) + \
                "d" + str(self.dealerScore) + \
                "m" + str(self.moveName).upper())

    def __eq__(self, other):
        return int(self.playerScore) == int(other.getPlayerScore()) and \
                int(self.dealerScore) == int(other.getDealerScore()) and \
                str(self.moveName).lower() == str(other.getMoveName()).lower()

if __name__ == '__main__':
    from RolloutKey import RolloutKey

    dictRollout = {}
    aKey1 = RolloutKey(10, "H", 17)
    aKey4 = RolloutKey(10, "H", 19)
    aKey2 = RolloutKey(10, "S", 20)
    aKey3 = RolloutKey(19, "H", 20)
    aKey5 = RolloutKey(19, "H", 20)

    print not aKey1 == aKey2
    print aKey1, aKey2

    assert not aKey1 == aKey2
    assert aKey3 == aKey5

    dictRollout[aKey1] = (1,0,0)
    dictRollout[aKey2] = (0,1,0)
    dictRollout[aKey3] = (0,1,0)
    print dictRollout.has_key(aKey3), dictRollout.has_key(aKey5)
    dictRollout[aKey3] = (0,1,0)

    print dictRollout