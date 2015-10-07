from Hand import Hand

class Player(object):

    def __init__(self, idName, bankAccountStart, numDecks):
        self.idName = idName
        self.bankAccountBalance = bankAccountStart
        self.canHit = True
        self.currentCards = Hand([])
        self.cardCountList = [0]*11
        self.currentBet = 0
        self.numDecks = numDecks

    def __eq__(self, other):
        return self.idName == other.getName()

    def getName(self):
        return self.idName

    def __repr__(self):
        return ("Player: " + str(self.idName) + "\n\tBank: " + str(self.bankAccountBalance) + \
            "\n\tCan Hit: " + str(self.canHit) + "\n\tCurrent Cards: " + str(self.currentCards) + "\n\tCard Count list: " +\
            str(self.cardCountList) + "\n\tBet: " + str(self.currentBet))

    # Adds a card to the player's hand
    def getCard(self, card):
        self.getHand().addCard(card)
        # self.countCard(card)

    # Counts a card the player has received
    def countCard(self, card):
        #If the card is a face card
        if(card.getValue() > 10):
            self.cardCountList[10] += 1
        else:
            self.cardCountList[card.getValue()] += 1

    # Gets the current player's hand
    def getHand(self):
        return self.currentCards

    # Gets the listing of counted cards cheater
    def getCardCounts(self):
        return self.cardCountList

    def getProbCardList(self):
        emptyList = [0]*11
        for i in range(1, len(self.cardCountList)):
            if(not i == len(self.cardCountList)-1):
                emptyList[i] = self.cardCountList[i]/float(4*self.numDecks)
            else:
                emptyList[i] = self.cardCountList[i]/float(16*self.numDecks)

        return emptyList

    # Sets a player's hand
    def setHand(self, newHand):
        self.currentCards = newHand

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
        if(self.currentBet * 2 <= self.bankAccountBalance):
            self.currentBet *= 2
        else:
            self.currentBet = self.bankAccountBalance

    # Gets the visible cards in a Hand
    def getVisibleHand(self):
        hand = self.getHand()
        visibleCards = []
        for aCard in hand.getCardList():
            if(aCard.getIsVisible()):
                visibleCards.append(aCard)

        return visibleCards

if __name__ == '__main__':
    from Card import Card
    aPlayer = Player("Ted", 100, 6) # 6 decks

    aCard1 = Card(Card.ACE, Card.H, True)
    print "ACE card: ", aCard1
    aCard2 = Card(Card.QUEEN, Card.S, True)
    aCard3 = Card(Card.KING, Card.D, True)
    aCard4 = Card(7, Card.C, True)

    print aPlayer

    print "-"*15, "Adding cards:", "-"*15
    aPlayer.getCard(aCard1)
    aPlayer.getCard(aCard2)
    aPlayer.getCard(aCard3)
    aPlayer.getCard(aCard4)
    print aPlayer

    print "-"*15, "Now let's give and take $", "-"*15
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

    print "-"*15, "Now let's double down", "-"*15
    print "Starting with 200 and bet of 100"
    aPlayer.setBankAccount(200)
    aPlayer.setBet(100)
    print aPlayer
    aPlayer.doDoubleDown()
    print aPlayer

    print "*"*50
    listOfProbs = aPlayer.getProbCardList()
    print listOfProbs, sum(listOfProbs)