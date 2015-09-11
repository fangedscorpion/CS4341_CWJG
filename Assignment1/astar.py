import sys
from World import World
from AStar2Fun import AStar2

# this function tests if a given path of Nodes has a start Node
# INPUT -> (list of Nodes) path
# OUTPUT -> (boolean)


def pathHasStart(path):
    for node in path:
        if node.getCell().getIsStart():
            return True
    return False

# this function calculates the score from the visited list
# INPUT -> (list of Nodes) visited
# OUTPUT -> (int) score


def getScore(vis):
    score = 100  # score starts at 100 for reaching the goal

    for node in vis:
        for turn in node.getActionList():
            score -= turn.getTimeCost()

    return score

# this function returns the number of actions in the path
# INPUT -> (list of Nodes) path
# OUTPUT -> (int) score


def getActions(pth):
    count = 0

    for node in pth:
        for turn in node.getActionList():
            count += 1

    return count


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Structure is: python astar.py filename.txt <heuristic function integer>"
    else:
        filename = sys.argv[1]
        heuristic = sys.argv[2]

        the_world = World(open(filename, "r"), heuristic)
        visited = AStar2(the_world)

        for visitNode in visited:
            print "*" * 20
            print visitNode

        path = [visited[len(visited) - 1]]
        while not pathHasStart(path):
            path.append(path[len(path) - 1].getParent())

        path.reverse()
        print "-----"
        # The score
        print "The score of expansion:",
        print getScore(visited)
        print

        print "The score of path:",
        print getScore(path)
        print

        # Number of actions
        print "The number of actions required to reach the goal:",
        print getActions(path)
        print

        # Number of nodes expanded
        print "The number of nodes expanded:",
        print len(visited)
        print

        # The series of actions
        print "The series of actions:"
        # print "\nPATH COORDS: "
        # for node in path:
        #     print node.getCell().getCoord()

        # print "\nPATH ACTIONS: "
        for node in path:
            acts = node.getActionList()
            for act in acts:
                print act
