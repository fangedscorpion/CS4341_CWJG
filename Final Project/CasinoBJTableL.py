from Shoe import Shoe
from Player import Player
from Dealer import Dealer
from Move import Move
from DealerMove import DealerMove
from StaticBJLogger import StaticBJLogger
from StaticBJGameLogger import StaticBJGameLogger
from random import shuffle
from ROPlayer import ROPlayer
from CCPlayer import CCPlayer
from BSPlayer import BSPlayer
from GameMove import GameMove
from DateTimeCustom import DateTimeCustom
from Hand import Hand


class CasinoBJTable(object):
    DEBUG = False
    ROLLOUTS = False

    def __init__(self, numDecks, numPlayers):
        self.numDecks = numDecks
        self.deck = Shoe(numDecks)
        self.dealer = Dealer(Dealer.bankStart, numDecks)
        self.playersList = []
        self.numPlayers = numPlayers
        for i in range(0, numPlayers):
            if CasinoBJTable.ROLLOUTS:
                playerPerson = Player(i, Player.startingBank, numDecks)
                self.playersList.append(playerPerson)
            else:
                self.playersList.append(
                    ROPlayer(i, Player.startingBank, numDecks, "MEGA_DICT.bin"))
                self.playersList.append(
                    BSPlayer(i, Player.startingBank, numDecks))
                self.playersList.append(
                    CCPlayer(i, Player.startingBank, numDecks))
                # self.playersList.append(Dealer(Dealer.bankStart, numDecks))
                shuffle(self.playersList)

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

            if CasinoBJTable.DEBUG:
                StaticBJLogger.writeDealerMove(DealerMove(
                    "TEST" + str(pl.getHands()[0].getHandValue()), pl.getHands()[counter]))  # Move.NOTCOMPLETE))
            while moreHands:
                old = len(pl.getHands())
                while counter < len(pl.getHands()):
                    if CasinoBJTable.DEBUG:
                        print "counter:", counter

                    keepGoing = True
                    while keepGoing == True:
                        if CasinoBJTable.DEBUG:
                            keepGoing = pl.play(counter)
                        else:
                            keepGoing = pl.play(
                                counter, self.dealer.getVisibleHand(0).getHandValue())
                        if keepGoing == True:
                            newCard = self.deck.getTopCard()
                            pl.getHands()[counter].addCard(newCard)
                            self.updatePlayers(newCard)
                            if CasinoBJTable.ROLLOUTS:
                                StaticBJLogger.writeDealerMove(DealerMove(
                                    self.dealer.getVisibleHand(0).getHandValue(), Move.NOTCOMPLETE))

                    counter += 1
                if CasinoBJTable.DEBUG:
                    print "OUT"
                moreHands = (old != len(pl.getHands()))

        keepGoing = True
        while keepGoing == True:
            keepGoing = self.dealer.play(None, None)

            if keepGoing == True:
                newCard = self.deck.getTopCard()
                self.dealer.getHands()[0].addCard(newCard)
                self.updatePlayers(newCard)

        if (CasinoBJTable.ROLLOUTS):
            if(len(pl.getHands()) == 2):
                if(self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust() and pl.getHands()[1].isBust()):
                    StaticBJLogger.writeDealerMove(DealerMove(
                        self.dealer.getHands()[0].getHandValue(), Move.NOTCOMPLETE))
                elif(self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust() and not pl.getHands()[1].isBust()):
                    StaticBJLogger.writeDealerMove(DealerMove(
                        self.dealer.getHands()[0].getHandValue(), Move.WON_BOTH))
                elif(self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust() and not pl.getHands()[1].isBust()):
                    StaticBJLogger.writeDealerMove(DealerMove(
                        self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_2))
                elif(self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust() and pl.getHands()[1].isBust()):
                    StaticBJLogger.writeDealerMove(DealerMove(
                        self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))
                elif(not self.dealer.getHands()[0].isBust() and (pl.getHands()[0].isBust() and pl.getHands()[1].isBust())):
                    StaticBJLogger.writeDealerMove(DealerMove(
                        self.dealer.getHands()[0].getHandValue(), Move.LOST))
                elif(not self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust() and pl.getHands()[1].isBust()):
                    if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[0].getHandValue()):
                        StaticBJLogger.writeDealerMove(DealerMove(
                            self.dealer.getHands()[0].getHandValue(), Move.LOST))
                    else:
                        StaticBJLogger.writeDealerMove(DealerMove(
                            self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))
                elif(not self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust() and not pl.getHands()[1].isBust()):
                    if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[1].getHandValue()):
                        StaticBJLogger.writeDealerMove(DealerMove(
                            self.dealer.getHands()[0].getHandValue(), Move.LOST))
                    else:
                        StaticBJLogger.writeDealerMove(DealerMove(
                            self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_2))
                elif(not self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust() and not pl.getHands()[1].isBust()):
                    if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[0].getHandValue()):
                        if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[1].getHandValue()):
                            StaticBJLogger.writeDealerMove(DealerMove(
                                self.dealer.getHands()[0].getHandValue(), Move.LOST))
                        else:
                            StaticBJLogger.writeDealerMove(DealerMove(
                                self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_2))
                    else:
                        if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[1].getHandValue()):
                            StaticBJLogger.writeDealerMove(DealerMove(
                                self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))
                        else:
                            StaticBJLogger.writeDealerMove(DealerMove(
                                self.dealer.getHands()[0].getHandValue(), Move.WON_BOTH))

            else:
                # House rules: tie on a bust for dealer and player
                if(self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust()):
                    StaticBJLogger.writeDealerMove(DealerMove(
                        self.dealer.getHands()[0].getHandValue(), Move.NOTCOMPLETE))
                elif(self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust()):
                    StaticBJLogger.writeDealerMove(DealerMove(
                        self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))
                elif(not self.dealer.getHands()[0].isBust() and pl.getHands()[0].isBust()):
                    StaticBJLogger.writeDealerMove(DealerMove(
                        self.dealer.getHands()[0].getHandValue(), Move.LOST))
                elif(not self.dealer.getHands()[0].isBust() and not pl.getHands()[0].isBust()):
                    if(self.dealer.getHands()[0].getHandValue() >= pl.getHands()[0].getHandValue()):
                        StaticBJLogger.writeDealerMove(DealerMove(
                            self.dealer.getHands()[0].getHandValue(), Move.LOST))
                    else:
                        StaticBJLogger.writeDealerMove(DealerMove(
                            self.dealer.getHands()[0].getHandValue(), Move.WON_HAND_1))
        else:
            for pl in self.playersList:
                gm = GameMove()

                for val in pl.getHandsVals():
                    if val > 21:
                        gm.incBust()
                    elif val > self.dealer.getHands()[0].getHandValue():
                        gm.incWon()
                    else:
                        gm.incLoss()

                if isinstance(pl, BSPlayer):
                    if CasinoBJTable.DEBUG:
                        print "BS"
                    StaticBJGameLogger.writeBSMove(gm)
                elif isinstance(pl, ROPlayer):
                    if CasinoBJTable.DEBUG:
                        print "RO"
                    StaticBJGameLogger.writeROMove(gm)
                elif isinstance(pl, CCPlayer):
                    if CasinoBJTable.DEBUG:
                        print "CC"
                    StaticBJGameLogger.writeCCMove(gm)
                elif isinstance(pl, Dealer):
                    if CasinoBJTable.DEBUG:
                        print "Dealer"
                    StaticBJGameLogger.writeDealerMove(gm)
                else:
                    if CasinoBJTable.DEBUG:
                        "wah wah"

    def initPlayers(self):
        for i in range(0, 2):
            for pl in self.playersList:
                newCard = self.deck.getTopCard()
                pl.getHands()[0].addCard(newCard)
                self.updatePlayers(newCard)

            if(i == 1):  # Hide the dealers other card
                topCard = self.deck.getTopCard()
                topCard.setIsVisible(False)
                self.dealer.getHands()[0].addCard(topCard)
            else:
                newCard = self.deck.getTopCard()
                self.dealer.getHands()[0].addCard(newCard)
                self.updatePlayers(newCard)

    def resetPlayers(self):
        for pl in self.playersList:
            pl.setHand([Hand([])])
            pl.hasDouble = False
            pl.hasSplit = False
        self.dealer.setHand([Hand([])])

    def __repr__(self):
        strPlayers = ""
        for i in range(0, self.numPlayers):
            strPlayers += str(self.playersList[i])
            strPlayers += "\n"
        return (strPlayers)

    # plays blackjack till a specific time
    # day, hour, minute is the ending time for the function
    def play(self, day, hour, minute):
        endTime = DateTimeCustom(day, hour, minute)
        self.resetPlayers()
        while not endTime.greaterEqualTo():
            if self.deck.yellowCardPassed():
                del self.deck
                self.deck = Shoe(self.numDecks)

            self.initPlayers()
            self.playRound()
            self.resetPlayers()

if __name__ == '__main__':
    from StaticBJLogger import StaticBJLogger
    from StaticBJGameLogger import StaticBJGameLogger
    from Card import Card
    # StaticBJLogger.init(1)      # for rollouts
    StaticBJGameLogger.init(0)  # for full game
    table = CasinoBJTable(6, 1)
    table.initPlayers()
    # table.playersList[0].hands[0].cardList = [
    #     Card(7, Card.S, True), Card(7, Card.H, True)]
    table.play(14, 17, 10)
