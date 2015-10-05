""" This class represents a deck of 52 cards """

from Card import Card
from random import shuffle
from copy import deepcopy


class Deck(object):
    TOTAL = 52
    SUIT = 4
    CARDS = 13

    def __init__(self):
        self.cards = []

        for i in range(0, Deck.SUIT):
            for j in range(0, Deck.CARDS):
                if (i == 0):
                    self.cards.append(Card(j + 1, Card.D, True))
                elif (i == 1):
                    self.cards.append(Card(j + 1, Card.H, True))
                elif (i == 2):
                    self.cards.append(Card(j + 1, Card.C, True))
                else:
                    self.cards.append(Card(j + 1, Card.S, True))

        shuffle(self.cards)

    def setDeck(self, list):
        self.cards = list

    def getDeck(self):
        return deepcopy(self.cards)

    def __repr__(self):
        string = ""

        for j in range(0, len(self.cards)):
            string += str(self.cards[j]) + "\n"

        return string

if __name__ == "__main__":
    ad = Deck()
    print ad
