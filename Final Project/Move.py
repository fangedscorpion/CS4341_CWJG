
class Move(object):

    BUSTED = 1
    NOTBUSTED = 0

    SHORTEN_MOVE_NAMES = 1

    NOTCOMPLETE = -1
    LOST = 0
    WON_HAND_1 = 1
    WON_HAND_2 = 2
    WON_BOTH = 3

    SPLITNUM = -2
    NOTSPLIT = 0

    SPLIT = "Split"
    HIT = "Hit"
    DOUBLE = "Double"
    STAY = "Stay"

    SPLIT_SHORT = "S"
    HIT_SHORT = "H"
    DOUBLE_SHORT = "D"
    STAY_SHORT = "Y"

    def __init__(self, playerCnt, moveStrName, bustedOrNot, split):
        self.playerCnt = playerCnt

        if(Move.SHORTEN_MOVE_NAMES == 1):
            if(moveStrName == Move.SPLIT):
                self.moveStrName = Move.SPLIT_SHORT
            elif(moveStrName == Move.HIT):
                self.moveStrName = Move.HIT_SHORT
            elif(moveStrName == Move.DOUBLE):
                self.moveStrName = Move.DOUBLE_SHORT
            elif(moveStrName == Move.STAY):
                self.moveStrName = Move.STAY_SHORT
        else:
            self.moveStrName = moveStrName
            
        self.bustedOrNot = bustedOrNot
        self.split = split

    # Simple code
    def __repr__(self):
        return (str(self.playerCnt) + "," + str(self.moveStrName) + "," +
                str(self.bustedOrNot) + "," + str(self.split) + ",")

if __name__ == '__main__':
    from Move import Move

    aMove = Move(10, "Hit",     Move.BUSTED,        Move.NOTCOMPLETE)
    aMove2 = Move(19, "Stay",   Move.NOTBUSTED,     Move.NOTCOMPLETE)
    aMove3 = Move(18, "Hit",    Move.BUSTED,        Move.WON)
    # Breaks into two hands being played
    aMove4 = Move(18, "Split",  Move.NOTBUSTED,     Move.SPLITNUM)

    print aMove
    print aMove2
    print aMove3
    print aMove4
