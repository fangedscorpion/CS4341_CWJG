
class Move(object):

    BUSTED = 1
    NOTBUSTED = 0
    MAXHANDS = 2
    SPLIT = "Split"
    HIT = "Hit"
    DOUBLE = "Double"
    STAY = "Stay"

    def __init__(self, playerCnt, moveStrName, bustedOrNot, split):
        self.playerCnt = playerCnt
        self.moveStrName = moveStrName
        self.bustedOrNot = bustedOrNot
        self.split = split

    # Simple code
    def __repr__(self):
        return (str(self.playerCnt) +","+ str(self.moveStrName) + "," + \
            str(self.bustedOrNot) + "," + str(self.split)+",")

if __name__ == '__main__':
    from Move import Move

    aMove = Move(10, "Hit", 0, 0)
    aMove2 = Move(19, "Stay", 0, 0)
    aMove3 = Move(18, "Hit", 1, 0)
    aMove4 = Move(18, "Split", 0, 2) # Breaks into two hands being played

    print aMove
    print aMove2
    print aMove3
    print aMove4