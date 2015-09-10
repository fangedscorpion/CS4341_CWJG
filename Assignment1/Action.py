class Action:

    """This class is a simple represetation of the various actions the robot can take"""
    actionName = ""  # A String name
    timeCost = -1  # The time cost of the action

    def __init__(self, actionName, timeCost):
        self.actionName = actionName
        self.timeCost = timeCost

    def getTimeCost(self):
        return self.timeCost

    def getActionName(self):
        return self.actionName

    def __repr__(self):
        string = "Name: " + \
            str(self.actionName) + ". Cost: " + str(self.timeCost)
        return string

if __name__ == "__main__":
    actionDebug = Action("Debug Action", 30)
    print actionDebug
