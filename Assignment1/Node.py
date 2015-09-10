from Action import Action


class Node:

    """This is the class the represents the node of a path. This is like a path segment essentially"""

    def __init__(self, cell, actionList):
        self.currentCell = cell
        self.actionList = actionList
        self.costSoFar = self.sumCost()

    def getActionList(self):
        return self.actionList

    def getCurrentCell(self):
        return self.currentCell

    # this function totals the cost taken to get to this node
    # INPUT -> none
    # OUTPUT -> (int) total cost
    def sumCost(self):
        sum = 0
        for ac in self.actionList:
            sum += ac.getTimeCost()
        return sum

    # this function returns the cost of the most recent action taken to get to this cell
    # INPUT -> none
    # OUTPUT -> (int) cost
    def recentCost(self):
        return self.actionList[len(self.actionList) - 1].getTimeCost()

    # this function returns the action list
    # INPUT -> none
    # OUTPUT -> (list) self.actionList
    def getActionList(self):
        return self.actionList

if __name__ == "__main__":
    # a_node = Node("cell", ["turn"])
    # print a_node.getActionList(), a_node.getCurrentCell()
    # print "['turn']", "cell"
    # print

    aa = Action("bash", 3)
    ab = Action("fwd", 6)

    b_node = Node("a_cell", [aa, ab])
    print b_node.recentCost(), 6
    print b_node.sumCost(), 9
    print b_node.getActionList(), "[Action object, Action object]"
