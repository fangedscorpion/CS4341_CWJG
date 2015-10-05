""" This class represents a playing card. """


class Card(object):
    # Static variables representing face card value
    ACE = 1
    JACK = 11
    QUEEN = 12
    KING = 13

    # Static variables representing suits
    D = "diamond"
    H = "heart"
    C = "club"
    S = "spaid"

    # Static variables representing Ace relative values
    HIGH = "high"
    LOW = "low"

    def __init__(self, value, suit, isVisible, hl):
        self.value = value
        self.suit = suit
        self.isVisible = isVisible
        self.hl = hl

    def setValue(self, val):
        self.value = val

    def getValue(self):
        return self.value

    def setSuit(self, su):
        self.suit = su

    def getSuit(self):
        return self.suit

    def setIsVisible(self, vis):
        self.isVisible = vis

    def getIsVisible(self):
        return self.isVisible

    def isAce(self):
        return self.value == Card.ACE

    # input: HL "high" or "low" for aces
    def setHL(self, HL):
        self.hl = HL

    # output: returns if an ace is high or low
    def getHL(self):
        if self.isAce():
            return self.hl
        else:
            print "not an Ace"

    def isFaceCard(self):
        return self.value == Card.JACK or self.value == Card.QUEEN or self.value == Card.KING

    def __repr__(self):
        return "" + str(self.value) + " " + str(self.suit)

if __name__ == "__main__":
    a = Card(Card.ACE, Card.S, True)
    t = Card(2, Card.D, False)
    j = Card(Card.JACK, Card.S, True)
    q = Card(Card.QUEEN, Card.S, True)
    k = Card(Card.KING, Card.S, True)

    print a.isAce(), True
    print j.isAce(), False
    print j.isFaceCard(), True
    print q.isFaceCard(), True
    print k.isFaceCard(), True
    print a.isFaceCard(), False

    a.setValue(3)
    print a.getValue(), 3

    a.setSuit(Card.C)
    print a.getSuit(), "club"

    print a.getIsVisible(), True
    a.setIsVisible(False)
    print a.getIsVisible(), False

    print t, "2 diamond"
