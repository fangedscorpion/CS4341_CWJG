from Action import Action
from math import ceil

class TurnAction(Action):

    """This is a more sophisticated turn Action"""

    def __init__(self, cellComplexity, strDir):
        Action.__init__(self, "Turn " + strDir, int(ceil(cellComplexity / 3.0)))
        self.strDir = strDir

    # INPUT: TurnAction
    # OUTPUT: String that is L or R
    def getStrDr(self):
    	return self.strDir

if __name__ == "__main__":
    a_turn = TurnAction(3, "R")

    print str(a_turn)
    assert str(a_turn) == "Name: Turn R. Cost: 1", True
