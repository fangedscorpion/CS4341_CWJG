from Action import Action


class Node:

    """This is the class the represents the node of a path. This is like a path segment essentially"""

    def __init__(self, cell, parentNode, actionList, cost):
        self.currentCell = cell
        self.actionList = actionList
        self.parentNode = parentNode
        self.cost = cost + self.sumActionList(self.actionList)

    # this function sums and returns the total time cost of the list
    # INPUT -> (list of Actions)
    # OUTPUT -> (int) sum
    def sumActionList(self, a_list):
        sum = 0
        for alpha in a_list:
            sum += alpha.getTimeCost()
        return sum

    # This function returns the parent node
    # INPUT -> none
    # OUTPUT -> (Node) self.parentNode
    def getParent(self):
        return self.parentNode

    # This function changes the parent node
    # INPUT -> (Node) parent
    # OUTPUT -> none
    def setParent(self, parent):
        self.parentNode = parent

    def getActionList(self):
        return self.actionList

    def getCurrentCell(self):
        return self.currentCell

    # this function returns the cost so far to the node
    # INPUT -> none
    # OUTPUT -> (int)
    def getCost(self):
        return self.cost

    # this function adds a given action to the actionList
    # the function also adds the new action's cost to the node's cost
    # INPUT -> (Action)
    # OUTPUT -> none
    def addAction(self, newAction):
        self.actionList.append(newAction)
        self.cost += newAction.getTimeCost()

    # this function removes the most recently added action from the actionList
    # the function then returns the removed action
    # INPUT -> none
    # OUTPUT -> (Action)
    def removeAction(self):
        alpha = self.actionList.pop(len(self.actionList) - 1)
        self.cost -= alpha.getTimeCost()
        return alpha

    # This function checks to see if a bash was used in this Node
    # INPUT -> none
    # OUTPUT -> (boolean)
    def didIBash(self):
        for ac in self.actionList:
            if (ac.getActionName().lower() == "bash"):
                return True
        return False

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

    # this function returns a boolean if the most recent move was a bash
    # INPUT -> none
    # OUTPUT -> (boolean)
    def justBashed(self):
        return self.actionList[len(self.actionList) - 1].getActionName().lower() == "bash"

if __name__ == "__main__":
    from Bash import Bash
    from FwdAction import FwdAction
    from TurnAction import TurnAction

    a_node = Node("cell", "parentA", [FwdAction(4)], 6)
    print a_node.getCost(), 10
    print a_node.getActionList()
    print "**"

    a_node.addAction(TurnAction(6))
    print a_node.getActionList()
    print a_node.getCost(), 12
    print a_node.didIBash(), False
    print "**"

    a_node.addAction(Bash())
    print a_node.getActionList()
    print a_node.getCost(), 15
    print a_node.didIBash(), True
    print "**"

    a_node.removeAction()
    print a_node.getActionList()
    print a_node.getCost(), 12
    print a_node.didIBash(), False

    assert a_node.getParent() == "parentA"
    a_node.setParent("parentB")
    assert a_node.getParent() == "parentB"
