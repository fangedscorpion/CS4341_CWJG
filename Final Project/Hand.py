from Card import Card
import copy


class Hand(object):

    def __init__(self, cardList):
        self.cardList = cardList  # the list of cards in a player's hand

    # overriding the equals (==) operator

    def __eq__(self, other):
        return self.cardList == other.cardList

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return "Hand:" + str(self.cardList)

    # input: -
    # output: returns the cardList of a hand
    def getCardList(self):
        return self.cardList

    # input: a card to add to the hand
    # output: -
    def addCard(self, newCard):
        self.cardList.append(newCard)

    # get total of hand without any aces
    # input: -
    # output: int
    def getTotalNoAce(self):
        total = 0
        for cd in self.getCardList():
            if not cd.isAce():
                total += cd.getValue()

        return total

    def getHandValue(self):
        handValue = 0
        for card in self.cardList:
            if card.isAce():
                if card.high:
                    handValue += 11
                else:
                    handValue += 1
            elif card.isFaceCard():
                handValue += 10
            else:
                handValue += card.getValue()
        return handValue

    # sets all cards in the hand as visible
    def showHiddenCards(self):
        for card in self.getCardList():
            card.setIsVisible(True)

    # used when splitting
    # only works if the hand has 2 cards of the same value
    # returns one of the cards and removes it from the hand list
    def popCard(self):
        if len(self.cardList) == 2:
            if self.cardList[0] == self.cardList[1]:
                popCard = copy.copy(self.cardList[1])
                # self.cardList.remove(popCard) #Real subtle logic error
                # removing my card because I redefined their equals method
                del self.cardList[1]
                return popCard
            else:
                print "cards are not equal, cant be split"
        else:
            print self.cardList
            print "have ", str(len(self.cardList)), " cards, cant split"

    # Returns a bool. true if the hand is bust, false if not.
    # if the hand contains a "high" ace, it will force it low
    def isBust(self):
        if self.getHandValue() > 21:
            for card in self.cardList:
                if card.isAce() and card.high:
                    card.high = False

        if self.getHandValue() > 21:
            return True
        else:
            return False

    # returns a boolean
    # true if the cards are of equal value and can be split
    # false if the cards are of unequal value and cannot be split
    def canSplit(self):
        if len(self.getCardList()) != 2:
            return False
        elif (self.getCardList()[0] != self.getCardList()[1]):
            return False
        else:
            return True

    # returns a boolean
    # true if the length is equal to 2
    # false otherwise
    def canDouble(self):
        return len(self.getCardList()) == 2

    # returns True if the hand contains +1 Ace
    # a soft hand is a hand with an ace
    # otherwise the hand is hard
    def isSoft(self):
        for cr in self.getCardList():
            if (cr.isAce()):
                return True

        return False

if __name__ == "__main__":
    emptyLine = "-" * 20
    a = Card(Card.ACE, Card.S, True)
    t = Card(2, Card.D, False)
    s = Card(7, Card.H, True)
    j = Card(Card.JACK, Card.S, True)
    q = Card(Card.QUEEN, Card.S, True)
    k = Card(Card.KING, Card.S, True)

    bustHand = Hand([j, q, k])
    perfectHand = Hand([a, j])
    lowAceHand = Hand([a, j, k])
    someHand = Hand([t, j])
    splitHand = Hand([s, s])
    bigHand = Hand([s, s, s])

    print emptyLine
    print "Copy test"
    copyHand = bustHand
    print "original:"
    print bustHand
    print "copy:"
    print copyHand
    print emptyLine

    print "getCardList test:"
    print someHand.getCardList()
    print emptyLine

    print "addCard() test:"
    print someHand
    someHand.addCard(s)
    print someHand
    print emptyLine

    print "isSoft test:"
    print bustHand.isSoft(), False
    print perfectHand.isSoft(), True
    print emptyLine

    print "getHandValue() test:"
    print someHand.getHandValue()
    print "getHandValue() on ace high:"
    print perfectHand.getHandValue()
    print emptyLine

    print "showHiddenCards() test:"
    print str(someHand.getCardList()[0].getIsVisible())
    someHand.showHiddenCards()
    print str(someHand.getCardList()[0].getIsVisible())
    print emptyLine

    print "canSplit() test:"
    print splitHand.canSplit(), True
    print someHand.canSplit(), False
    print bigHand.canSplit(), False
    print emptyLine

    print "canDouble() test"
    print splitHand.canDouble(), True
    print bigHand.canDouble(), False
    print emptyLine

    print "popCard() test:"
    print "hand:"
    print splitHand
    print "card thats popped:"
    print splitHand.popCard()
    print "card left in hand:"
    print splitHand
    print "hand with 3 cards:"
    print bustHand.popCard()
    print "hand that doesnt have pair:"
    print perfectHand.popCard()
    print emptyLine

    print "isbust() test:"
    print "bust hand:"
    print str(bustHand.isBust())
    print "safe hand:"
    print str(someHand.isBust())
    print "hand that should be fixed to not be bust:"
    print str(lowAceHand.isBust())
    print emptyLine
