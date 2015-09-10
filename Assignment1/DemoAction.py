from Action import Action


class DemoAction(Action):

    """This is a more sophisticated forward Action"""

    def __init__(self):
        Action.__init__(self, "Demo", 4)

if __name__ == "__main__":
    a_turn = DemoAction()
    assert str(a_turn) == "Name: Demo. Cost: 4"
    assert a_turn.getTimeCost() == 4
