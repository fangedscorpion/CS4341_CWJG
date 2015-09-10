class TurnAction(Action):

    """This is a more sophisticated turn Action"""

    def __init__(self):
        Action.init(self, "Turn", -1)
        print("Debug")

    def calculateTurnCost(self, currentCellVal):
        print("Define how to calculate the turn cost")

if __name__ == "__main__":
    print("Something debuggy here")
