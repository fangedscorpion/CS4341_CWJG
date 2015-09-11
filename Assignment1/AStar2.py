
def AStar2(world):  # start and goal are cells
    print "running AStar2"

    robotDir = 0
    start = world.getStart()
    goal = world.getGoal()

    frontier = []  # nodes
    visited = []  # nodes

    firstNode = Node(start, Cell(Coord(-1, -1), -1), [], 0)

    frontier.append(firstNode)

    while len(frontier) is not 0:
        # HOPEFULLY ths sorts the list so that the least g+h is first
        frontier.sort(key=lambda node: node.total())
        # after frontier is sorted the node with the lowest g+h becomes current
        print "------------------------------"
        print "len of frontier" 
        print len(frontier)
        current = frontier[0]
        if(current.getCell() is goal):  # if its the goal, we are done
            visited.append(current)
            print "Goal Found!"
            return visited

        # remove the node being looked at from the frontier
        frontier.remove(current)
        visited.append(current)  # add it to the visited list

        neighborCells = world.getNeighbors(current.getCell().getCoord())
        neighborNodes = cellsToNodes(current, neighborCells, robotDir, False)

        print "len of neighborNodes" 
        print len(neighborNodes)
        for neighborNode in neighborNodes:
            if not neighborNode in visited:
                for frontNode in frontier:
                    if neighborNode in frontier:
                        if neighborNode.getCost() < frontNode.getCost():
                            frontier.remove(frontNode)
                        else:
                            neighborNodes.remove(neighborNode)
                            break
            else:
                neighborNodes.remove(neighborNode)

 
        frontier += neighborNodes

        for neighborNode in neighborNodes:
            frontier.append(neighborNode)

        bashCells = world.getBashNeighbors(current.getCell().getCoord())
        bashNodes = cellsToNodes(current, bashCells, robotDir, True)

        for bashNode in bashNodes:
            if not bashNode in visited:
                for frontNode in frontier:
                    if bashNode.getCell().getCoord() is frontNode.getCell().getCoord():
                        if bashNode.getCost() < frontNode.getCost():
                            frontier.remove(frontNode)
                        else:
                            bashNodes.remove(bashNode)
                            break
            else:
                bashNodes.remove(bashNode)

        frontier += bashNodes

    print "Goal not found!"



# takes in the current direction, the direction of the
# cell to be entered, and the complexities (com) of both cells
# and returns the action list for moving from the first cell
# to the next cell
def getAction(curDir, cellDir, curCom, cellCom, bashHuh):
    delta = curDir - cellDir
    if not bashHuh:
        if delta is 0:  # no turn
            return [FwdAction(cellCom)]
        elif delta is -1 or 3:  # right turn
            return [TurnAction(curCom, "r"), FwdAction(cellCom)]
        elif delta is 1 or -3:  # left turn
            return [TurnAction(curCom, "l"), FwdAction(cellCom)]
        elif delta is 2 or -2:  # 180
            return [TurnAction(curCom, "r"), TurnAction(curCom, "r"), FwdAction(cellCom)]
    if bashHuh:
        if delta is 0:  # no turn
            return [Bash(), FwdAction(cellCom)]
        elif delta is -1 or 3:  # right turn
            return [TurnAction(curCom, "r"), Bash(), FwdAction(cellCom)]
        elif delta is 1 or -3:  # left turn
            return [TurnAction(curCom, "l"), Bash(), FwdAction(cellCom)]
        elif delta is 2 or -2:  # 180
            return [TurnAction(curCom, "r"), TurnAction(curCom, "r"), Bash(), FwdAction(cellCom)]


# takes in the current node, the list of cells neighboring the
# current node, and the direction of the robot and returns
# a list of all VALID nodes constructed from the cells
def cellsToNodes(currCell, listOfCells, robotDir, bashHuh):
    newNodes = []
    for j in range(0, len(listOfCells)):
        if not listOfCells[j].IsValid():
            continue

        curCom = currCell.getCell().getComplexity()
        cellCom = listOfCells[j].getComplexity()
        currCellAction = getAction(robotDir, j, curCom, cellCom, bashHuh)
        # make a node based on the
        newNode = Node(listOfCells[j], currCell, currCellAction, currCell.getCost())
        newNodes.append(newNode)
    return newNodes

if __name__ == "__main__":

    from World import *
    from Node import *
    from Cell import *
    from FwdAction import *
    from TurnAction import *
    from Bash import *
    from Coord import *

    testWorld = World(open("test_board.txt", "r"))
    print "World Constructed"

    AStar2(testWorld)
