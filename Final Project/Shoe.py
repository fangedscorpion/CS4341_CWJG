""" This class represents a Shoe """
from random import randint
from random import shuffle
from Deck import Deck


class Shoe(object):

    def __init__(self, numDecks):
        listOfDecks = []
        for i in range(0, numDecks):
            listOfDecks.append(Deck())

        self.deck = []
        for j in range(0, len(listOfDecks)):
            self.deck += listOfDecks[j].getDeck()

        shuffle(self.deck)

        self.yellowCard = randint(
            (3 * len(self.deck)) / 5, (4 * len(self.deck)) / 5)

    def __repr__(self):
        string = ""

        for j in range(0, len(self.deck)):
            string += str(self.deck[j]) + "\n"

        return string

    # pops the upcoming card from the deck and returns it
    def getTopCard(self):
        return self.deck.pop(0)

    # this function returns a boolean if the yellow card has passed or is the next card
    # this is the cue to shuffle
    # INPUT - none
    # OUTPUT - boolea
    def yellowCardPassed(self):
        return len(self.deck) <= self.yellowCard

if __name__ == "__main__":
    aS = Shoe(2)
    aS.yellowCard = 100
    print len(aS.deck)
    print aS.getTopCard(), len(aS.deck), 103, aS.yellowCardPassed(), False
    print aS.getTopCard(), len(aS.deck), 102, aS.yellowCardPassed(), False
    print aS.getTopCard(), len(aS.deck), 101, aS.yellowCardPassed(), False
    print aS.getTopCard(), len(aS.deck), 100, aS.yellowCardPassed(), True
    print aS.getTopCard(), len(aS.deck), 99, aS.yellowCardPassed(), True