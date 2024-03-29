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
    S = "spades"

    # Static variables representing Ace relative values
    HIGH = "high"
    LOW = "low"

    def __init__(self, value, suit, isVisible):
        self.value = value
        self.suit = suit
        self.isVisible = isVisible
        self.high = True

    # overrides ==
    # tests based upon value only
    def __eq__(self, other):
        if(self.value >= 10 and other.value >= 10):
	       return True
        else:  
            return self.value == other.value

    # overrides !=
    # tests based upon value only
    def __ne__(self, other):
	return not self == other

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

    # input: High = true, low = false
    def setHigh(self, HighOrLow):
        self.hl = HighOrLow

    # output: returns if an ace is high or low
    def getHL(self):
        if self.isAce():
            return self.high
        else:
            print "not an Ace"

    def isFaceCard(self):
        return self.value == Card.JACK or self.value == Card.QUEEN or self.value == Card.KING

    def __repr__(self):
        return "" + str(self.value) + " " + str(self.suit)

if __name__ == "__main__":
    a = Card(Card.ACE, Card.S, True)
    t = Card(2, Card.D, False)
    tt = Card(2, Card.S, True)
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

    print t == tt, True
    print t != tt, False
    print t == a, False
    print t != a, True
