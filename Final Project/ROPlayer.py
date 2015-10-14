from Player import Player
from Card import Card
from RolloutKey import RolloutKey
from BJGetter import BJGetter
import pickle

class ROPlayer(Player):

    def __init__(self, idName, bankAccountStart, numDecks, pickleName):
        super(ROPlayer, self).__init__(idName, bankAccountStart, numDecks)
        self.dict = pickle.load(open(pickleName, "rb"))



    def play(self, Hand, dealerShow):

        return self.bestMove(Hand,dealerShow, self.dict)

    def getWinPerc(aKey, aDict):
        wins = aDict[aKey][0]
        losses = aDict[aKey][1]
        unfinished = aDict[aKey][2]

        totalPlayed = float(wins + losses)
        return (wins / totalPlayed)

    def bestMove(self, Hand, dealerShow):
        myHand = self.getHands()[Hand]
        if not myHand.isBust():
            myHitKey = RolloutKey(myHand, 'H', dealerShow)
            hitChance = getWinPerc(myHitKey, self.dict)
        else:
            #if hand busted, return stay
            return False

        myStayKey = RolloutKey(myHand, 'S', dealerShow)
        stayChance = getWinPerc(myStayKey, self.dict) 

        if aHand.canDouble():
            myDDKey = RolloutKey(myHand, 'D', dealerShow)
            ddChance = getWinPerc(myDDKey, self.dict)
        else: 
            ddChance = 0

        if aHand.canSplit():
            mySplitKey = RolloutKey(myHand,'Y', dealerShow)
            splitChance = getWinPerc(mySplitKey, self.dict) 
        else:
            splitChance = 0

        chances = [hitChance, stayChance, ddChance, splitChance]
        moves = ['H', 'S', 'D', 'Y']
        
        bestChance = 0
        bestMove = 'S'
        for i in range(len(chances)):
            if chances[i] > bestChance:
                bestMove = moves[i]

        
        if bestMove == 'H':
            return True
        elif bestMove == 'D':
            self.doDoubleDown()
            return True
        elif bestMove == 'Y':
            self.doSplit(Hand)
            return True
        else:
            #stay
            return False

if __name__ == '__main__':
    # aROP = ROPlayer("Ted", 100, 6, "BJStats_302.txt")



        
        