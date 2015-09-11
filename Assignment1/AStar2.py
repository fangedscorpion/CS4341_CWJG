
def AStar2(world):  # start and goal are cells
    print "running AStar2"

    robotDir = 0
    start = world.getStart()
    goal = world.getGoal()
    print goal.getCoord()

    frontier = []  # nodes
    visited = []  # nodes

    firstNode = Node(start, Cell(Coord(-1, -1), -1), [], 0)

    frontier.append(firstNode)

    while len(frontier) is not 0:
        # HOPEFULLY ths sorts the list so that the least g+h is first
        frontier.sort(key=lambda node: node.total())
        # after frontier is sorted the node with the lowest g+h becomes current
        print "------------------------------"
        # print "len of frontier"
        # print len(frontier)
        current = frontier[0]
        if(current.getCell() is goal):  # if its the goal, we are done
            visited.append(current)
            print "Goal Found!"
            return visited

        # remove the node being looked at from the frontier
        frontier.remove(current)
        

        visited.append(current)  # add it to the visited list
        print anydup(visited)
        # raw_input()

        neighborCells = world.getNeighbors(current.getCell().getCoord())
        neighborNodes = cellsToNodes(current, neighborCells, robotDir, False)
#uncommenting this
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
#uncommented to here
#commenting below
        # for j in range(0, len(neighborNodes)):
        #     # if neighborNodes[j] in visited:
        #     if inList(visited, neighborNodes[j]):
        #         pass
        #     else:
        #         # if neighborNodes[j] in frontier:
        #         if inList(frontier, neighborNodes[j]):
        #             for k in range(0, len(frontier)):
        #                 if (neighborNodes[j]) == frontier[k]:
        #                     if neighborNodes[j].total() < frontier[k].total:
        #                         frontier[k] = neighborNodes[j]
        #                         print "added:", neighborNodes[j].getCell().getCoord()
        #         else:
        #             frontier.append(neighborNodes[j])
        #             print "added:", neighborNodes[j].getCell().getCoord()

        # print "errrthing"
        # for an in visited:
        #     print an.getCell().getCoord()
#commented up to here
        bashCells = world.getBashNeighbors(current.getCell().getCoord())
        bashNodes = cellsToNodes(current, bashCells, robotDir, True)
#uncommenting below
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
#to here
        for j in range(0, len(bashNodes)):
            # if bashNodes[j] in visited:
            if inList(visited, bashNodes[j]):
                pass
            else:
                # if bashNodes[j] in frontier:
                if inList(frontier, bashNodes[j]):
                    for k in range(0, len(frontier)):
                        if (bashNodes[j]) == frontier[k]:
                            if bashNodes[j].total() < frontier[k].total:
                                frontier[k] = bashNodes[j]
                                print "added:", bashNodes[j].getCell().getCoord()
                else:
                    frontier.append(bashNodes[j])
                    print "added:", bashNodes[j].getCell().getCoord()

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
        newNode = Node(
            listOfCells[j], currCell, currCellAction, currCell.getCost())
        newNodes.append(newNode)
    return newNodes

def anydup(thelist):
    for x in range(0, len(thelist)):
        for y in range(x, len(thelist)):
            if x==y:
                return True
    return False

def inList(thelist, node):
    for x in range(0, len(thelist)):
        if (thelist[x].getCell().getCoord().getX() == node.getCell().getCoord().getX()) and (thelist[x].getCell().getCoord().getY() == node.getCell().getCoord().getY()):
            return True
    return False


if __name__ == "__main__":

    from World import *
    from Node import *
    from Cell import *
    from FwdAction import *
    from TurnAction import *
    from Bash import *
    from Coord import *

    def pathHasStart(path):
        for node in path:
            if node.getCell().getIsStart():
                return True
        return False

    testWorld = World(open("test_board.txt", "r"))
    print "World Constructed"

    visited = AStar2(testWorld)
    print visited[len(visited)-1].getCell().getComplexity()
    path = [visited[len(visited) - 1]]
    while not pathHasStart(path):
        path.append(path[len(path) - 1].getParent())
        print "working..."
    print "done"

    path.reverse()
    for node in path:
        print node.getCell().getCoord()
