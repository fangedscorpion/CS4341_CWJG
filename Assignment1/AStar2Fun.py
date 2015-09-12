from World import *
from Node import *
from Cell import *
from FwdAction import *
from TurnAction import *
from Bash import *
from Coord import *
def AStar2(world, DEBUG_MODE):  # start and goal are cells

    if(DEBUG_MODE == 1):
        print "running AStar2"

    start = world.getStart()
    goal = world.getGoal()
    if(DEBUG_MODE == 1):
        print goal.getCoord()

    frontier = []  # nodes
    visited = []  # nodes

    numberMoves = 0

    firstNode = Node(start, Cell(Coord(-1, -1), -1), [], 0, 0) # Last 0 is robot dir!

    frontier.append(firstNode)

    while len(frontier) is not 0:
        # HOPEFULLY ths sorts the list so that the least g+h is first
        frontier.sort(key=lambda node: node.total())
        # for node in frontier:
            # print node
        # after frontier is sorted the node with the lowest g+h becomes current

        current = frontier[0]
        # remove the node being looked at from the frontier
        del frontier[0]
        visited.append(current)  # add it to the visited list

        if(DEBUG_MODE == 1):
            print "------------------------------"
            print "len of frontier"
            print len(frontier)
            print "len of visited"
            print len(visited)
            
            print "current Coords"
            print current.getCell().getCoord()

        if(current.getCell().getIsGoal()):  # if its the goal, we are done
            if(DEBUG_MODE == 1):
                print "Goal Found!"
            return (visited, numberMoves)

        # print anydup(visited)
        # raw_input()

        if(DEBUG_MODE == 1):
            print "Building neighbors..."

        neighborCells = world.getNeighbors(current.getCell().getCoord())
        neighborNodes = cellsToNodes(current, neighborCells, current.getRobotDir(), False)
        bashCells = world.getBashNeighbors(current.getCell().getCoord())
        bashNodes = cellsToNodes(current, bashCells, current.getRobotDir(), True)
        moveNodes = list(neighborNodes + bashNodes)

        numberMoves += len(moveNodes)
        
        if(DEBUG_MODE == 1):
            print len(moveNodes)

        neibsRm = []
        frontRm = []
        for i in range(len(moveNodes)):
            neighborNode = moveNodes[i]
            for j in range(len(visited)):
                visitNode = visited[j]
                if neighborNode.getCell().getCoord() != visitNode.getCell().getCoord(): # I think This is where we are accidentally adding tons of things to visited
                    for f in range(len(frontier)):
                        frontNode = frontier[f]
                        if neighborNode.getCell().getCoord() == frontNode.getCell().getCoord():
                            if neighborNode.total() < frontNode.total():
                                frontRm.append(f)
                            else:
                                neibsRm.append(i)
                else:
                    neibsRm.append(i)

        removedFront = 0
        for rm in list(set(frontRm)):
            if(DEBUG_MODE == 1):
                print "FrontRM:",rm - removedFront
            del frontier[rm - removedFront]
            removedFront += 1

        removedNeibs = 0
        for rm in list(set(neibsRm)):
            if(DEBUG_MODE == 1):
                print "MovesRM:",rm - removedNeibs
            del moveNodes[rm - removedNeibs]
            removedNeibs += 1

        if(DEBUG_MODE == 1):
            print "len of moveNodes"
            print len(moveNodes)
        frontier += moveNodes


    if(DEBUG_MODE == 1):
        print "Goal not found!"
    return ([], numberMoves)


# takes in the current direction, the direction of the
# cell to be entered, and the complexities (com) of both cells
# and returns the action list for moving from the first cell
# to the next cell
def getAction(curDir, cellDir, curCom, cellCom, bashHuh):
    robotDirTmp = curDir
    delta = curDir - cellDir
    if not bashHuh:
        if delta is 0:  # no turn
            return ([FwdAction(cellCom)], robotDirTmp)
        elif delta == -1 or delta == 3:  # right turn
            robotDirTmp += 1
            if robotDirTmp == 4:
                robotDirTmp = 0
            return ([TurnAction(curCom, "r"), FwdAction(cellCom)], robotDirTmp)
        elif delta == 1 or delta == -3:  # left turn
            robotDirTmp -= 1
            if robotDirTmp == -1:
                robotDirTmp = 3
            return ([TurnAction(curCom, "l"), FwdAction(cellCom)], robotDirTmp)
        elif delta == 2 or delta == -2:  # 180
            robotDirTmp += 2
            if robotDirTmp == 4:
                robotDirTmp = 0
            if robotDirTmp == 5:
                robotDirTmp = 1
            return ([TurnAction(curCom, "r"), TurnAction(curCom, "r"), FwdAction(cellCom)], robotDirTmp)
    if bashHuh:
        if delta is 0:  # no turn
            return ([Bash(), FwdAction(cellCom)], robotDirTmp)
        elif delta is -1 or 3:  # right turn
            robotDirTmp += 1
            if robotDirTmp == 4:
                robotDirTmp = 0
            return ([TurnAction(curCom, "r"), Bash(), FwdAction(cellCom)], robotDirTmp)
        elif delta is 1 or -3:  # left turn
            robotDirTmp -= 1
            if robotDirTmp == -1:
                robotDirTmp = 3
            return ([TurnAction(curCom, "l"), Bash(), FwdAction(cellCom)], robotDirTmp)
        elif delta is 2 or -2:  # 180
            robotDirTmp += 2
            if robotDirTmp == 4:
                robotDirTmp = 0
            if robotDirTmp == 5:
                robotDirTmp = 1
            return ([TurnAction(curCom, "r"), TurnAction(curCom, "r"), Bash(), FwdAction(cellCom)], robotDirTmp)


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
        # print "Rob axn: ", robotDir, " curDir: ", j
        (currCellAction, robotDirTmp) = getAction(robotDir, j, curCom, cellCom, bashHuh)
        # make a node based on the
        newNode = Node(
            listOfCells[j], currCell, currCellAction, currCell.getCost(), robotDirTmp)
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

    testWorld = World(open("test_board.txt", "r"), 4)
    # testWorld = World(open("Our_Worlds/world1_5.txt", "r"), 1)
    print "World Constructed"

    (visited, numMoves) = AStar2(testWorld, 1)
    print visited[len(visited)-1].getCell().getComplexity()
    path = [visited[len(visited) - 1]]
    while not pathHasStart(path):
        path.append(path[len(path) - 1].getParent())
        print "working..."
    print "done"

    path.reverse()
    for node in path:
        print node.getCell().getCoord()
