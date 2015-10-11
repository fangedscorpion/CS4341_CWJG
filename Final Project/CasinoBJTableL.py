from Shoe import Shoe
from Player import Player
from Dealer import Dealer
from Move import Move
from DealerMove import DealerMove
from StaticBJLogger import StaticBJLogger

class CasinoBJTable(object):
    DEBUG = True

    def __init__(self, numDecks, numPlayers):
        self.deck = Shoe(numDecks)
        self.dealer = Dealer(Dealer.bankStart, numDecks)
        self.playersList = []
        self.numPlayers = numPlayers
        for i in range(0, numPlayers):
            playerPerson = Player(i, Player.startingBank, numDecks)
            self.playersList.append(playerPerson)

    def givePlayerCard(self, player):
        aCard = self.deck.getTopCard()
        print "Giving the player: " + aCard
        player.getCard(aCard, 0)

    def updatePlayers(self, aCard):
        for i in range(0, self.numPlayers):
            self.playersList[i].countCard(aCard)

    def saveGameState(self):
        exit("Save Not implemented")

    def playRound(self):
        for pl in self.playersList:
            counter = 0
            moreHands = True
            # StaticBJLogger.writeDealerMove(DealerMove(
            #                     "TEST" + str(pl.getHands()[0].getHandValue()), pl.getHands()[counter]))#Move.NOTCOMPLETE))
            while moreHands:
                old = len(pl.getHands())
                while counter < len(pl.getHands()):
                    if CasinoBJTable.DEBUG:
                        print "counter:", counter

                    keepGoing = True
                    while keepGoing == True:
                        keepGoing = pl.play(counter)
                        if keepGoing == True:
                            pl.getHands()[counter].addCard(
                                self.deck.getTopCard())
                            StaticBJLogger.writeDealerMove(DealerMove(
                                self.dealer.getVisibleHand(0).getHandValue(), Move.NOTCOMPLETE))

                    counter += 1
                if CasinoBJTable.DEBUG:
                    print "OUT"
                moreHands = (old != len(pl.getHands()))

        keepGoing = True
        while keepGoing == True:
            keepGoing = self.dealer.play(None)

            if keepGoing == True:
                self.dealer.getHands()[0].addCard(self.deck.getTopCard())

        if(len(pl.getHands()) == 2):
            if(self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust() and pl.getHands()[1].isBust()):
                StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.NOTCOMPLETE))
            elif(self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust() and not pl.getHands()[1].isBust()):
                StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_BOTH))
            elif(self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust() and not pl.getHands()[1].isBust()):
                StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_2))
            elif(self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust() and pl.getHands()[1].isBust()):
                StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))
            elif(not self.dealer.getHands()[0].isBust() and (pl.getHands()[0].isBust() and pl.getHands()[1].isBust())):
                StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.LOST))
            elif(not self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust() and pl.getHands()[1].isBust()):
                if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[0].getHandValue()):
                    StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.LOST))    
                else:
                    StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))    
            elif(not self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust() and not pl.getHands()[1].isBust()):
                if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[1].getHandValue()):
                    StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.LOST))    
                else:
                    StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_2))    
            elif(not self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust() and not pl.getHands()[1].isBust()):
                if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[0].getHandValue()):
                    if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[1].getHandValue()):
                        StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.LOST))
                    else:
                        StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_2))
                else:
                    if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[1].getHandValue()):
                        StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))
                    else:
                        StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_BOTH))

        else:
            #House rules: tie on a bust for dealer and player
            if(self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust()):
                StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.NOTCOMPLETE))
            elif(self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust()):
                StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))
            elif(not self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust()):
                StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.LOST))
            elif(not self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust()):
                if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[0].getHandValue()):
                    StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.LOST))
                else:
                    StaticBJLogger.writeDealerMove(DealerMove(self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))


        

    def initPlayers(self):
        for i in range(0, 2):
            for pl in self.playersList:
                pl.getHands()[0].addCard(self.deck.getTopCard())

            if(i == 1): #Hide the dealers other card
                topCard = self.deck.getTopCard()
                topCard.setIsVisible(False)
                self.dealer.getHands()[0].addCard(topCard)
            else:
                self.dealer.getHands()[0].addCard(self.deck.getTopCard())

    def resetPlayers(self):
        for pl in self.playersList:
            pl.setHand(Hand([]))
            pl.hasDouble = False
            pl.hasSplit = False
        self.dealer.setHand(Hand([]))

    def __repr__(self):
        strPlayers = ""
        for i in range(0, self.numPlayers):
            strPlayers += str(self.playersList[i])
            strPlayers += "\n"
        return (strPlayers)

if __name__ == '__main__':
    from StaticBJLogger import StaticBJLogger
    from Card import Card
    StaticBJLogger.init(1)
    table = CasinoBJTable(6, 1)
    table.initPlayers()
    table.playersList[0].hands[0].cardList = [
        Card(7, Card.S, True), Card(7, Card.H, True)]
    table.playRound()
