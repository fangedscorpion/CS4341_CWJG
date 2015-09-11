global robotDir
robotDir = 0
from World import *
from Node import *
from Cell import *
from FwdAction import *
from TurnAction import *
from Bash import *
from Coord import *

def AStar2(world):  # start and goal are cells
    print "running AStar2"
    global robotDir

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
        for node in frontier:
            print node
        # after frontier is sorted the node with the lowest g+h becomes current
        print "------------------------------"
        print "len of frontier"
        print len(frontier)
        print "len of visited"
        print len(visited)
        current = frontier[0]
        print "current Coords"
        print current.getCell().getCoord()
        if(current.getCell().getIsGoal()):  # if its the goal, we are done
            visited.append(current)
            print "Goal Found!"
            return visited

        # remove the node being looked at from the frontier
        frontier.remove(current)
        visited.append(current)  # add it to the visited list

        # print anydup(visited)
        # raw_input()

        neighborCells = world.getNeighbors(current.getCell().getCoord())
        neighborNodes = cellsToNodes(current, neighborCells, robotDir, False)


        for neighborNode in neighborNodes:
            if not neighborNode in visited: # I think This is where we are accidentally adding tons of things to visited
                for frontNode in frontier:
                    if neighborNode.getCell().getCoord() == frontNode.getCell().getCoord():
                        if neighborNode.getCost() < frontNode.getCost():
                            frontier.remove(frontNode)
                            break
                        else:
                            print "Removing: " + str(neighborNode)
                            neighborNodes.remove(neighborNode)
                            break
            else:
                #print "Removing: " + str(neighborNode)
                neighborNodes.remove(neighborNode)

        print "len of neighborNodes"
        print len(neighborNodes)
        frontier += neighborNodes

        bashCells = world.getBashNeighbors(current.getCell().getCoord())
        bashNodes = cellsToNodes(current, bashCells, robotDir, True)

        for bashNode in bashNodes:
            if not bashNode in visited:
                for frontNode in frontier:
                    if bashNode.getCell().getCoord() == frontNode.getCell().getCoord():
                        if bashNode.getCost() < frontNode.getCost():
                            frontier.remove(frontNode)
                        else:
                            bashNodes.remove(bashNode)
                            break
            else:
                bashNodes.remove(bashNode)

        print "len of bashNodes"
        print len(bashNodes)
        frontier += bashNodes


    print "Goal not found!"


# takes in the current direction, the direction of the
# cell to be entered, and the complexities (com) of both cells
# and returns the action list for moving from the first cell
# to the next cell
def getAction(curDir, cellDir, curCom, cellCom, bashHuh):
    robotDirTmp = 0
    delta = curDir - cellDir
    if not bashHuh:
        if delta is 0:  # no turn
            return [FwdAction(cellCom)]
        elif delta == -1 or delta == 3:  # right turn
            robotDirTmp += 1
            print delta
            print robotDirTmp
            if robotDirTmp == 4:
                robotDirTmp = 0
            return [TurnAction(curCom, "r"), FwdAction(cellCom)]
        elif delta == 1 or delta == -3:  # left turn
            robotDirTmp -= 1
            if robotDirTmp == -1:
                robotDirTmp = 3
            return [TurnAction(curCom, "l"), FwdAction(cellCom)]
        elif delta == 2 or delta == -2:  # 180
            robotDirTmp += 2
            if robotDirTmp == 4:
                robotDirTmp = 0
            if robotDirTmp == 5:
                robotDirTmp = 1
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
        print "Rob axn: ", robotDir, " curDir: ", j
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

    testWorld = World(open("test_board.txt", "r"), 1)
    # testWorld = World(open("Our_Worlds/world1_1.txt", "r"), 1)
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
