from Shoe import Shoe
from Player import Player
from Dealer import Dealer
from Move import Move


class CasinoBJTable(object):

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
            counter = -1
            for hn in pl.getHands():
                counter += 1
                keepGoing = True
                while keepGoing == True:
                    keepGoing = pl.play(counter)

                    if keepGoing == True:
                        hn.addCard(self.deck.getTopCard())
                        StaticBJLogger.writeDealerMove(DealerMove(self.getHands()[0].getHandValue(), Move.NOTCOMPLETE))
        
        keepGoing = True
        while keepGoing == True:
            keepGoing = self.dealer.play(None)

            if keepGoing == True:
                self.dealer.getHands()[0].addCard(self.deck.getTopCard())

    def initPlayers(self):
        for i in range(0, 2):
            for pl in self.playersList:
                pl.getHands()[0].addCard(self.deck.getTopCard())
            self.dealer.getHands()[0].addCard(self.deck.getTopCard())

    def resetPlayers(self):
        for pl in self.playersList:
            pl.setHand(Hand([]))
        self.dealer.setHand(Hand([]))

    def __repr__(self):
        strPlayers = ""
        for i in range(0, self.numPlayers):
            strPlayers += str(self.playersList[i])
            strPlayers += "\n"
        return (strPlayers)

if __name__ == '__main__':
    from StaticBJLogger import StaticBJLogger
    StaticBJLogger.init(1)
    table = CasinoBJTable(6, 1)
    table.initPlayers()
    table.playRound()
