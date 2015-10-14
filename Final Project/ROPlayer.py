from Player import Player
from Card import Card
from Hand import Hand
from RolloutKey import RolloutKey
from BJGetter import BJGetter
import pickle

class ROPlayer(Player):

    def __init__(self, idName, bankAccountStart, numDecks, pickleName):
        super(ROPlayer, self).__init__(idName, bankAccountStart, numDecks)
        self.dict = pickle.load(open(pickleName, "rb"))



    def play(self, Hand, dealerShowVal):

        return self.bestMove(Hand,dealerShowVal)

    def getWinPerc(self, aKey, aDict):

        wins = aDict[aKey][0]
        losses = aDict[aKey][1]
        unfinished = aDict[aKey][2]

        totalPlayed = float(wins + losses)
        if totalPlayed == 0:
            winRate = 0
        else:
            winRate = (wins / totalPlayed)
        return winRate


    def bestMove(self, Hand, dealerShowVal):
        hitChance = 0
        stayChance = 0
        ddChance = 0
        splitChance = 0
        listOfKeys = []

        myHand = self.getHands()[Hand]
        if not myHand.isBust():
            myHitKey = RolloutKey(myHand.getHandValue(), "H", dealerShowVal)
            listOfKeys.append(myHitKey)
            if myHitKey in self.dict.keys():
                hitChance = self.getWinPerc(myHitKey, self.dict)
        else:
            #if hand busted, return stay
            return False

        myStayKey = RolloutKey(myHand.getHandValue(), "S", dealerShowVal)
        listOfKeys.append(myStayKey)
        if myStayKey in self.dict.keys():
            stayChance = self.getWinPerc(myStayKey, self.dict) 

        if myHand.canDouble():
            myDDKey = RolloutKey(myHand.getHandValue(), "D", dealerShowVal)
            listOfKeys.append(myDDKey)
            if myDDKey in self.dict.keys():
                ddChance = self.getWinPerc(myDDKey, self.dict)
        else: 
            ddChance = 0

        if myHand.canSplit():
            mySplitKey = RolloutKey(myHand.getHandValue(),"Y", dealerShowVal)
            listOfKeys.append(mySplitKey)
            if mySplitKey in self.dict.keys():
                splitChance = self.getWinPerc(mySplitKey, self.dict) 
        else:
            splitChance = 0

        for key in listOfKeys:
            if key not in self.dict.keys():
                if key == myHitKey:
                    hitChance = 0.25
                if key == myStayKey:
                    stayChance = 0.25

        chances = [hitChance, stayChance, ddChance, splitChance]
        moves = ["H", "S", "D", "Y"]
        
        bestChance = 0
        bestMove = "S"
        for i in range(len(chances)):
            if chances[i] > bestChance:
                bestMove = moves[i]

        
        if bestMove == "H":
            return True
        elif bestMove == "D":
            self.doDoubleDown()
            return True
        elif bestMove == "Y":
            self.doSplit(Hand)
            return True
        else:
            #stay
            return False

if __name__ == '__main__':

    a = Card(Card.ACE, Card.S, True)
    t = Card(2, Card.D, False)
    s = Card(7, Card.H, True)
    j = Card(Card.JACK, Card.S, True)
    q = Card(Card.QUEEN, Card.S, True)
    k = Card(Card.KING, Card.S, True)
    d = Card(10, Card.S, True)
    dd = Card(Card.KING, Card.H, True)
    ddd = Card(7, Card.H, True)

    someHand = Hand([ddd,t, j])


    Ted = ROPlayer("Ted", 100, 6, "dict1.7_mil.p")
    Ted.setHand([someHand])

    Ted.play(0, 8)

        