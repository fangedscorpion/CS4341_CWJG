from Action import Action

class TurnAction(Action):

    """This is a more sophisticated turn Action"""

    def __init__(self, cellComplexity):
        Action.__init__(self, "Turn", (cellComplexity / 3))

if __name__ == "__main__":
    a_turn = TurnAction(3)
    print a_turn
    print "Name: Turn. Cost: 1"
    print
    print a_turn.getTimeCost(), 1
