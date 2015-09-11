from World import *
from Node import *
from Cell import *
from FwdAction import *
from TurnAction import *
from Bash import *
from Coord import *

def AStar2(world):  # start and goal are cells
    print "running AStar2"

    start = world.getStart()
    goal = world.getGoal()
    print goal.getCoord()

    frontier = []  # nodes
    visited = []  # nodes

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
        frontier.remove(current)
        visited.append(current)  # add it to the visited list

        print "------------------------------"
        print "len of frontier"
        print len(frontier)
        print "len of visited"
        print len(visited)
        
        print "current Coords"
        print current.getCell().getCoord()
        if(current.getCell().getIsGoal()):  # if its the goal, we are done
            visited.append(current)
            print "Goal Found!"
            return visited



        # print anydup(visited)
        # raw_input()

        print "Building neighbors..."
        neighborCells = world.getNeighbors(current.getCell().getCoord())
        neighborNodes = cellsToNodes(current, neighborCells, current.getRobotDir(), False)
        bashCells = world.getBashNeighbors(current.getCell().getCoord())
        bashNodes = cellsToNodes(current, bashCells, current.getRobotDir(), True)
        moveNodes = neighborNodes + bashNodes


        for moveNode in moveNodes: #for each possible move from the current cell
            for visitNode in visited: #see if that move would put us in a cell thats already been visited
                if moveNode.getCell().getCoord() is not visitNode.getCell().getCoord(): #if we've not visited this cell before
                    for frontNode in frontier: #ee if the move would put us in a cell that is already in the frontier
                        if moveNode.getCell().getCoord() is frontNode.getCell().getCoord(): # if it is
                            if moveNode.getCost() < frontNode.getCost(): # check if the new move is cheaper than the old move
                                frontier.remove(frontNode) # if it is, remove the old move from frontier
                                break
                            else: # otherwise, remove the new node from the list of nodes that will be added to frontier
                                # print "Removing: " + str(moveNode)
                                if moveNode in moveNodes:
                                    moveNodes.remove(moveNode)
                                break
                else: # if the node we are looking at would put us in a cell thats already been visited
                    #print "Removing: " + str(moveNode)
                    if moveNode in moveNodes:
                        moveNodes.remove(moveNode) # remove the new node  from the list of nodes to be added to the frontier

        print "len of moveNodes"
        print len(moveNodes)
        frontier += moveNodes


    print "Goal not found!"


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

    testWorld = World(open("test_board.txt", "r"), 1s)
    # testWorld = World(open("Our_Worlds/world1_5.txt", "r"), 1)
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
