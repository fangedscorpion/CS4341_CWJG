from Hand import Hand
import random
from StaticBJLogger import StaticBJLogger
from Move import Move
from CC import CC

class Player(object):
    startingBank = 500

    PlayerDebug = False

    def __init__(self, idName, bankAccountStart, numDecks):
        self.idName = idName
        self.bankAccountBalance = bankAccountStart
        self.canHit = True
        self.hands = [Hand(([]))]
        self.myCC = CC(numDecks)
        self.currentBet = 0
        self.numDecks = numDecks
        self.hasSplit = False
        self.hasDouble = False

    def __eq__(self, other):
        return self.idName == other.getName()

    def getName(self):
        return self.idName

    def __repr__(self):
        return ("Player: " + str(self.idName) + "\n\tBank: " + str(self.bankAccountBalance) +
                "\n\tCan Hit: " + str(self.canHit) + "\n\tCurrent Cards: " + str(self.hands) + "\n\tCard Count list: " +
                str(self.cardCountList) + "\n\tBet: " + str(self.currentBet))

    # Adds a card to the player's hand
    # handNum is the hand number to add the card, indexed from 0
    def getCard(self, card, handNum):
        self.getHands()[handNum].addCard(card)
        # self.countCard(card)

    # Counts a card the player has received
    def countCard(self, card):
        self.myCC.update(card.getValue())

    # determines if a player can split his/her hand
    # returns a boolean
    # def canSplit(self, handNum):
    #     return (self.getHands()[handNum].getHandValue() % 2 == 0)

    # Gets the current player's hands
    def getHands(self):
        return self.hands

    def getHandsVals(self):
        handVals = []
        for i in range(len(self.getHands())):
            handVals.append(self.getHands()[i].getHandValue())
        return handVals

    def getProbCardList(self):
        emptyList = [0] * 11
        for i in range(1, len(self.cardCountList)):
            if(not i == len(self.cardCountList) - 1):
                emptyList[i] = self.cardCountList[i] / float(4 * self.numDecks)
            else:
                emptyList[i] = self.cardCountList[
                    i] / float(16 * self.numDecks)

        return emptyList

    # Sets a player's hand
    def setHand(self, newHand):
        self.hands = newHand

    # adds a hand to a player's list of hands
    def addHand(self, newHand):
        hands = self.getHands()[0]
        self.setHand([hands, newHand])

    # Get the players bank account and win big
    def getBankAccount(self):
        return self.bankAccountBalance

    # Drain their bank account now
    def setBankAccount(self, newAmount):
        self.bankAccountBalance = newAmount

    # Get the bet information
    def getBet(self):
        return self.currentBet

    # Set the bet amount (GO BIG)
    # Limits it to the size of the bankAccountBalance
    def setBet(self, newBet):
        if(newBet <= self.bankAccountBalance):
            self.currentBet = newBet
        else:
            self.currentBet = self.bankAccountBalance

    # Updates the player's bank account given their bet
    def updateBank(self, wonBool):
        if(wonBool):
            self.bankAccountBalance += self.currentBet
        else:
            self.bankAccountBalance -= self.currentBet

    # double down makes the player's bet double
    # Limits to the bank account balance
    def doDoubleDown(self):
        self.hasDouble = True
        if(self.currentBet * 2 <= self.bankAccountBalance):
            self.currentBet *= 2
        else:
            self.currentBet = self.bankAccountBalance

    # Gets the visible cards in a Hand
    def getVisibleHand(self, hand):
        handTmp = self.getHands()[hand]
        visibleCards = []
        for aCard in handTmp.getCardList():
            if(aCard.getIsVisible()):
                visibleCards.append(aCard)

        return Hand(list(visibleCards))

    # does a split move for the currect player
    # modifications to player's bet needs to be added
    def doSplit(self, hand):
        self.hasSplit = True
        self.addHand(Hand([self.getHands()[hand].popCard()]))

    # This function does 1 move for the player
    # hand is an integer for the hand being played
    # hand is indexed from 0
    def play(self, hand):
        found = False  # flag if a move as been performed
        print self.getHands()
        if (len(self.getHands()[hand].getCardList()) == 1):
            if (Player.PlayerDebug):
                print "BALANCE"

            return True

        while not found:
            number = random.randint(0, 3)  # random move to do

            if (number == 0) or (self.getHands()[hand].isBust()) or (self.hasDouble):
                # stay
                if (Player.PlayerDebug):
                    print "STAY"

                if(self.hasSplit):
                    if (self.getHands()[hand].isBust()):
                        StaticBJLogger.writePlayerMove(
                            Move(self.getHands()[hand].getHandValue(), Move.STAY, Move.BUSTED, hand + 1))
                    else:
                        StaticBJLogger.writePlayerMove(
                            Move(self.getHands()[hand].getHandValue(), Move.STAY, Move.NOTBUSTED, hand + 1))
                else:
                    if (self.getHands()[hand].isBust()):
                        StaticBJLogger.writePlayerMove(Move(
                            self.getHands()[hand].getHandValue(), Move.STAY, Move.BUSTED, Move.NOTSPLIT))
                    else:
                        StaticBJLogger.writePlayerMove(Move(
                            self.getHands()[hand].getHandValue(), Move.STAY, Move.NOTBUSTED, Move.NOTSPLIT))

                # Reset the split variable if needed
                if(self.hasSplit and hand == len(self.getHands())):
                    self.hasSplit = False

                return False
            elif (number == 1) and self.getHands()[hand].canSplit() and (len(self.getHands()) == 1):
                # split
                if (Player.PlayerDebug):
                    print "SPLIT"

                StaticBJLogger.writePlayerMove(Move(
                    self.getHands()[hand].getHandValue(), Move.SPLIT, Move.NOTBUSTED, Move.SPLITNUM))
                # print "BEFORE SPLIT: ", self.getHands()[hand]
                self.doSplit(hand)
                # print "POST SPLIT: ", self.getHands()[hand]

                return True
            elif (number == 2) and (self.getHands()[hand].canDouble()):
                # double
                if (Player.PlayerDebug):
                    print "DOUBLE"

                self.doDoubleDown()
                if(self.hasSplit):
                    StaticBJLogger.writePlayerMove(Move(
                        self.getHands()[hand].getHandValue(), Move.DOUBLE, Move.NOTBUSTED, hand + 1))
                else:
                    StaticBJLogger.writePlayerMove(Move(self.getHands()[hand].getHandValue(
                    ), Move.DOUBLE, Move.NOTBUSTED, Move.NOTSPLIT))
                return True
            else:
                # hit
                if (Player.PlayerDebug):
                    print "HIT"

                if(self.hasSplit):
                    StaticBJLogger.writePlayerMove(
                        Move(self.getHands()[hand].getHandValue(), Move.HIT, Move.NOTBUSTED, hand + 1))
                else:
                    StaticBJLogger.writePlayerMove(Move(
                        self.getHands()[hand].getHandValue(), Move.HIT, Move.NOTBUSTED, Move.NOTSPLIT))
                return True

if __name__ == '__main__':
    from Card import Card

    aPlayer = Player("Ted", 100, 6)  # 6 decks

    aCard1 = Card(Card.ACE, Card.H, True)
    print "ACE card: ", aCard1
    aCard2 = Card(Card.QUEEN, Card.S, True)
    aCard3 = Card(Card.KING, Card.D, True)
    aCard4 = Card(7, Card.C, True)
    aCard5 = Card(7, Card.H, True)

    print aPlayer

    print "-" * 15, "Adding cards:", "-" * 15
    aPlayer.getCard(aCard1, 0)
    aPlayer.getCard(aCard2, 0)
    aPlayer.getCard(aCard3, 0)
    aPlayer.getCard(aCard4, 0)
    print aPlayer

    print "-" * 15, "Now let's give and take $", "-" * 15
    print "Giving the lucky guy 50"
    aPlayer.setBankAccount(aPlayer.getBankAccount() + 50)
    print aPlayer
    print "Take all the $$$$!!!"
    aPlayer.setBankAccount(0)
    print aPlayer
    aPlayer.setBankAccount(200)
    print "GO BIG WITH A BET"
    aPlayer.setBet(100)
    print aPlayer
    print "Lost that bet"
    aPlayer.updateBank(False)
    print aPlayer

    print "-" * 15, "Now let's double down", "-" * 15
    print "Starting with 200 and bet of 100"
    aPlayer.setBankAccount(200)
    aPlayer.setBet(100)
    print aPlayer
    aPlayer.doDoubleDown()
    print aPlayer

    print "*" * 50
    listOfProbs = aPlayer.getProbCardList()
    print listOfProbs, sum(listOfProbs)

    aPlayer2 = Player("Teo", 100, 6)  # 6 decks
    aPlayer2.getCard(aCard4, 0)
    aPlayer2.getCard(aCard5, 0)
    print aPlayer2
    aPlayer2.play(0)
    print aPlayer2
    aPlayer2.play(0)
    print aPlayer2
    aPlayer2.play(0)
    print aPlayer2
