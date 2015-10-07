from Shoe import Shoe
from Player import Player

class CasinoBJTable(object):

    def __init__(self, numDecks, numPlayers):
        self.deck = Shoe(numDecks)
        self.playersList = []
        self.numPlayers = numPlayers
        for i in range(0, numPlayers):
            playerPerson = Player(i, 500, numDecks)
            self.playersList.append(playerPerson)

    def givePlayerCard(self, player):
        aCard = self.deck.getTopCard()
        print "Giving the player: " + aCard
        player.getCard(aCard)

    def updatePlayers(self, aCard):
        for i in range(0, self.numPlayers):
            self.playersList[i].countCard(aCard)

    def saveGameState(self):
        exit("Save Not implemented")

    def __repr__(self):
        strPlayers = ""
        for i in range(0, self.numPlayers):
            strPlayers += str(self.playersList[i])
            strPlayers += "\n"
        return (strPlayers) 

if __name__ == '__main__':
    table = CasinoBJTable(6, 2)
    print "Players: \n", table


