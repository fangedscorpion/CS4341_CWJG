from Player import Player
from Card import Card
from Hand import Hand
from CC import CC

class CCPlayer(Player):

    def __init__(self, idName, bankAccountStart, numDecks):
        super(CCPlayer, self).__init__(idName, bankAccountStart, numDecks)
        self.myCC = CC(numDecks)

    def reset(self):
        myCC.reset()

    def countCard(self, card):
        self.myCC.update(card)

    def play(self):

        if (self.getHands()[0].getHandValue() + self.myCC.getEV() > 21):
            #stay
            return False
        else:
            #hit
            return True


if __name__ == '__main__':
    aCCP = CCPlayer("Ted", 100, 6)


