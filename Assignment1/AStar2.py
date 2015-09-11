
def AStar2(world):  # start and goal are cells
    print "running AStar2"

    robotDir = 0
    start = world.getStart()
    print "a* bitch -> ", start
    goal = world.getGoal()

    frontier = []  # nodes
    visited = []  # nodes

    firstNode = Node(start, Cell(Coord(-1, -1), -1), [], 0)

    frontier.append(firstNode)

    while frontier is not []:
        # HOPEFULLY ths sorts the list so that the least g+h is first
        frontier.sort(key=lambda node: node.total())
        # after frontier is sorted the node with the lowest g+h becomes current
        current = frontier[0]
        if(current.cell is goal):  # if its the goal, we are done
            return reconstructPath()  # this will be a thing

        # remove the node being looked at from the frontier
        frontier.remove(current)
        visited.append(current)  # add it to the visited list

        neighborCells = world.getNeighbors(current.getCell())
        neighborNodes = cellsToNodes(current, neighborCells, robotDir, False)

        for neighborNode in neighborNodes:
            for frontNode in frontier:
                if neighborNode.getCell().getCoord() is frontNode.getCell().getCoord():
                    if neighborNode.getCost() < frontNode.getCost():
                        frontier.remove(frontNode)
                        frontier.append(neighborNode)
                    else:
                        continue
                else:
                    frontier.append(neighborNode)

        bashCells = world.getBashNeighbors(current.getCell())
        bashNodes = cellsToNodes(current, bashCells, robotDir, True)

        for bashNode in bashNodes:
            for frontNode in frontier:
                if bashNode.getCell.getCoord() is frontNode.getCell().getCoord():
                    if neighborNode.getCost() < frontNode.getCost():
                        frontier.remove(frontNode)
                        frontier.append(bashNode)
                    else:
                        continue
                else:
                    frontier.append(bashNode)


# takes in the current direction, the direction of the
# cell to be entered, and the complexities (com) of both cells
# and returns the action list for moving from the first cell
# to the next cell
def getAction(curDir, cellDir, curCom, cellCom, bashHuh):
    delta = curDir - cellDir
    if not bashHuh:
        if delta is 0:  # no turn
            return [fwdAction(cellCom)]
        elif delta is -1 or 3:  # right turn
            return [turn(curCom, "r"), fwdAction(cellCom)]
        elif delta is 1 or -3:  # left turn
            return [turn(curCom, "l"), fwdAction(cellCom)]
        elif delta is 2 or -2:  # 180
            return [turn(curCom, "r"), turn(curCom, "r"), fwdAction(cellCom)]
    if bashHuh:
        if delta is 0:  # no turn
            return [bash(), fwdAction(cellCom)]
        elif delta is -1 or 3:  # right turn
            return [turn(curCom, "r"), bash(), fwdAction(cellCom)]
        elif delta is 1 or -3:  # left turn
            return [turn(curCom, "l"), bash(), fwdAction(cellCom)]
        elif delta is 2 or -2:  # 180
            return [turn(curCom, "r"), turn(curCom, "r"), bash(), fwdAction(cellCom)]


# takes in the current node, the list of cells neighboring the
# current node, and the direction of the robot and returns
# a list of all VALID nodes constructed from the cells
def cellsToNodes(currrent, listOfCells, robotDir, bashHuh):
    newNodes = []
    for j in range(0, len(listOfCells)):
        if not listOfCells[j].IsValid():
            continue

        curCom = current.getCell().getComplexity()
        cellCom = listOfCells[j].getComplexity()
        currentAction = getAction(robotDir, j, curCom, cellCom, bashHuh)
        # make a node based on the
        newNode = Node(
            listOfCells[j], current, currentAction, current.getCost())
        newNodes.append(newNode)
    return newNodes

if __name__ == "__main__":

    from World import *
    from Node import *
    from Cell import *

    testWorld = World(open("test_board.txt", "r"))
    print "World Constructed"

    AStar2(testWorld)
