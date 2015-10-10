class DealerMove(object):

    def __init__(self, dealerCardSum, playerWon):
        self.dealerCardSum = dealerCardSum
        self.playerWon = playerWon

    # Simple code
    def __repr__(self):
        return (str(self.dealerCardSum) + "," + str(self.playerWon))\

if __name__ == '__main__':
    from DealerMove import DealerMove

    aMove = DealerMove(10, -1)
    aMove2 = DealerMove(16, -1)
    aMove3 = DealerMove(22, 1)

    print aMove
    print aMove2
    print aMove3
