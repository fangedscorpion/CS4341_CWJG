from Player import Player
from Card import Card

class BSPlayer(Player):

    def __init__(self, idName, bankAccountStart, numDecks):
        super(idName, bankAccountStart, numDecks)

    # follows basic strategy
    # https://www.blackjackinfo.com/blackjack-basic-strategy-engine/?numdecks=6&soft17=s17&dbl=all&das=yes&surr=ns&peek=yes
    # returns True if the dealer should deal a card
    # hand is an int for the hand number
    # dealerShow is an int for the card the dealer is showing
    def playBS(self, hand, dealerShow):
        if (len(self.getHands()[hand].getCardList())):
            return True

        # split cases
        if (self.getHands()[hand].canSplit()):
            value = self.getHands()[hand].getCardList()[0].getValue()
            if ((value == 2) or (value == 3)):
                if ((dealerShow == 2) or (dealerShow == 3) or (dealerShow == 4) or (dealerShow == 5) or (dealerShow == 6) or (dealerShow == 7)):
                    # split
                    self.doSplit()
                    return True
                else:
                    # hit
                    return True
            if (value == 4):
                if ((dealerShow == 5) or (dealerShow == 6)):
                    # split
                    self.doSplit()
                    return True
                else:
                    # hit
                    return True
            if (value == 5):
                if ((dealerShow == 10) or (dealerShow == Card.ACE)):
                    # hit
                    return True
                else:
                    # double
                    self.doDoubleDown()
                    return True
            if (value == 6):
                if ((dealerShow == 2) or (dealerShow == 3) or (dealerShow == 4) or (dealerShow == 5) or (dealerShow == 6)):
                    # split
                    self.doSplit()
                    return True
                else:
                    # hit
                    return True
            if (value == 7):
                if ((dealerShow == 8) or (dealerShow == 9) or (dealerShow == 10) or (dealerShow == Card.ACE)):
                    # hit
                    return True
                else:
                    # split
                    self.doSplit()
                    return True
            if (value == 8):
                self.doSplit()
                return True
            if (value == 9):
                if ((dealerShow == 7) or (dealerShow == 10) or (dealerShow == Card.ACE)):
                    # stay
                    return False
                else:
                    # split
                    self.doSplit()
                    return True
            if (value == 10):
                # stay
                return False
            if (value == Card.ACE):
                # split
                self.doSplit()
                return True
        # soft hand
        elif self.getHands()[hand].isSoft():
            value = self.getHands()[hand].getValueNoAce()
            if ((value == 2) or (value == 3)):
                if ((dealerShow == 5) or (dealerShow == 6)):
                    # double
                    self.doDoubleDown()
                    return True
                else:
                    # hit
                    return True
            if ((value == 4) or (value == 5)):
                if ((dealerShow == 4) or (dealerShow == 5) or (dealerShow == 6)):
                    # double
                    self.doDoubleDown()
                    return True
                else:
                    # hit
                    return True
            if (value == 6):
                if ((dealerShow == 3) or (dealerShow == 4) or (dealerShow == 5) or (dealerShow == 6)):
                    # double
                    self.doDoubleDown()
                    return True
                else:
                    # hit
                    return True
            if (value == 7):
                if ((dealerShow == 9) or (dealerShow == 10) or (dealerShow == Card.ACE)):
                    # hit
                    return True
                if ((dealerShow == 3) or (dealerShow == 4) or (dealerShow == 5) or (dealerShow == 6)):
                    # double
                    self.doDoubleDown()
                    return True
                else:
                    # split
                    return False
            if ((value == 8) or (value == 9) or (value == 10)):
                # split
                return False
        # hard hand
        else:
            value = self.getHands()[hand].getHandValue()
            if ((value == 5) or (value == 6) or (value == 7) or (value == 8)):
                # hit
                return True
            if (value == 9):
                if ((dealerShow == 3) or (dealerShow == 4) or (dealerShow == 5) or (dealerShow == 6)):
                    # double
                    self.doDoubleDown()
                    return True
                else:
                    # hit
                    return True
            if (value == 10):
                if ((dealerShow == 10) or (dealerShow == Card.ACE)):
                    # hit
                    return True
                else:
                    # double
                    self.doDoubleDown()
                    return True
            if (value == 11):
                if (dealerShow == Card.ACE):
                    # hit
                    return True
                else:
                    # double
                    self.doDoubleDown()
                    return True
            if (value == 12):
                if ((dealerShow == 4) or (dealerShow == 5) or (dealerShow == 6)):
                    # stay
                    return False
                else:
                    # hit
                    return True
            if ((value == 13) or (value == 14) or (value == 15) or (value == 16)):
                if ((dealerShow == 2) or (dealerShow == 3) or (dealerShow == 4) or (dealerShow == 5) or (dealerShow == 6)):
                    # stay
                    return False
                else:
                    # hit
                    return True
            else:
                # hit
                return True


if __name__ == '__main__':
    aBSP = BSPlayer("Ted", 100, 6)