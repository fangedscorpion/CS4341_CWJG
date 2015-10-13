from Player import Player
from Card import Card
from RolloutKey import RolloutKey

class ROPlayer(Player):

    def __init__(self, idName, bankAccountStart, numDecks, fileName):
        super(idName, bankAccountStart, numDecks)
        self.myBJGetter = bjGetter(fileName)


    def play(self, Hand, dealerShow):
        # get the dictionary reference for my hand
        myDict = self.myBJGetter.getDictionary()
        

        return self.bestMove(Hand,dealerShow, myDict)


    def bestMove(self, Hand,dealerShow):
        aHand = self.getHands[Hand]
        if not aHand.isBust():
            myHitKey = RolloutKey(myHand, 'H', dealerShow)
            hitChance = self.myBJGetter.getProbWinLost(myHitKey)[0]
        else:
            #if hand busted, return stay
            return False

        myStayKey = RolloutKey(myHand, 'S', dealerShow)
        stayChance = self.myBJGetter.getProbWinLost(myStayKey)[0]

        if aHand.canDouble():
            myDDKey = RolloutKey(myHand, 'D', dealerShow)
            ddChance = self.myBJGetter.getProbWinLost(myDDKey)[0]
        else: 
            ddChance = 0

        if aHand.canSplit():
            mySplitKey = RolloutKey(myHand,'Y', dealerShow)
            splitChance = slef.myBJGetter.getProbWinLost(mySplitKey)[0]
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
    aROP = ROPlayer("Ted", 100, 6, "BJStats_302.txt")



        
        