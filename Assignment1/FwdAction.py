from Action import Action


class FwdAction(Action):

    """This is a more sophisticated forward Action"""

    def __init__(self, cellComplexity):
        Action.__init__(self, "Fwd", cellComplexity)

if __name__ == "__main__":
    a_turn = FwdAction(3)
    print a_turn
    print "Name: Fwd. Cost: 3"
    print
    print a_turn.getTimeCost(), 3
