from Player import Player

class Dealer(Player):


    def __init__(self, bankAccountStart):
        Player.__init__(self, "Dealer", bankAccountStart)


        def showHiddenCard(self):
            self.currentCards.showHiddenCard()

        def play(self):
            if self.getHand().isBust():
                return False
            elif self.getHand().getHandValue() >= 17:
                return False
            else:
                return True

    def __repr__(self):
        print "Dealer:"
        # print self.getHand()


if __name__ == "__main__":
    from Card import Card

    a = Card(Card.ACE, Card.S, True)
    t = Card(2, Card.D, False)
    s = Card(7, Card.H, True)
    j = Card(Card.JACK, Card.S, True)
    q = Card(Card.QUEEN, Card.S, True)
    k = Card(Card.KING, Card.S, True)

    aDealer = Dealer(10000000)

    aDealer.getCard(s)
    aDealer.getCard(j)

    print aDealer


