from Player import Player
from StaticBJLogger import StaticBJLogger
from DealerMove import DealerMove


class Dealer(Player):
    bankStart = 0

    def __init__(self, bankAccountStart, numDecks):
        Player.__init__(self, "Dealer", bankAccountStart, numDecks)

    def showHiddenCard(self):
        self.currentCards.showHiddenCard()

    def play(self, num):
        if self.getHands()[0].isBust():
            StaticBJLogger.writeDealerMove(DealerMove(self.getHands()[0].getHandValue(), True))
            return False
        elif self.getHands()[0].getHandValue() >= 17:
            StaticBJLogger.writeDealerMove(DealerMove(self.getHands()[0].getHandValue(), False))
            return False
        else:
            return True

    def __repr__(self):
        return ("Dealer:" + str(Player.__repr__(self)))


if __name__ == "__main__":
    from Card import Card

    a = Card(Card.ACE, Card.S, True)
    t = Card(2, Card.D, False)
    s = Card(7, Card.H, True)
    j = Card(Card.JACK, Card.S, True)
    q = Card(Card.QUEEN, Card.S, True)
    k = Card(Card.KING, Card.S, True)

    aDealer = Dealer(10000000, 6)  # 6 decks

    aDealer.getCard(s, 0)
    aDealer.getCard(j, 0)

    print aDealer
