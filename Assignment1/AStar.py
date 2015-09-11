import sys
from World import World
from AStar2 import AStar2

# this function tests if a given path of Nodes has a start Node
# INPUT -> (list of Nodes) path
# OUTPUT -> (boolean)
def pathHasStart(path):
        for node in path:
            if node.getCell().getIsStart():
                return True
        return False

if __name__ == "__main__":
	if len(sys.argv) != 3:
		print "Structure is: python astar.py filename.txt <heuristic function integer>"
	else:
		filename = sys.argv[1]
		heuristic = sys.argv[2]

		the_world = World(open(filename, "r"), heuristic)
		visited = AStar2(the_world)
