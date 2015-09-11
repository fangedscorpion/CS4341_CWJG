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
		print "\nPATH COORDS: "
		for node in path:
		    print node.getCell().getCoord()

		print "\nPATH ACTIONS: "
		for node in path:
			acts = node.getActionList()
			for act in acts:
				print act