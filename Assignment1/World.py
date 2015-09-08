""" World Class """
""" Representation of all cells in the World """


class World(object):
    # file is the input world file
    # MakeWorld parses the input file and creates a list of a list of cells
    # self.start stores the starting cell to avoid using the function getStart() repeatidly
    # self.goal stores the goal cell to avoid using the function getGoal()
    # repeatidly

    def __init__(self, file):
        self.file = file
        self.world = self.MakeWorld(self.file)
        self.start = self.getStart()
        # self.goal = self.getGoal()

    # parses the input file and creates the world
    # INPUT -> (file) input world
    # OUTPUT -> (list of list of Cells) formatted world
    def MakeWorld(self, file):
    	# get all lines from input file
        lines = file.readlines()

        # split all idv input lines into lists
        for j in range(0, len(lines)):
            lines[j] = lines[j].split()

        # create list same size of the input grid
        world = [[0 for x in range(len(lines[0]))] for x in range(len(lines))] 

        # assign values from lines into world list
        for k in range(0, len(lines)):
            for l in range(0, len(lines[k])):
            	# replace 'lines[k][l]' with instanciation of Cell when Cell is defined
                world[k][l] = lines[k][l]

        # return world
        return world

    # parses through world looking for the starting cell
    # if no starting cell is found, returns -1
    # INPUT -> none
    # OUTPUT -> (cell) starting cell, OR (int) -1
    def getStart(self):
    	for j in range(0, len(self.world)):
    		for k in range(0, len(self.world[j])):
    			# if self.world[j][k].isStart():
    			# ^ switch boolean line when Cell is defined
    			if self.world[j][k] == "S":
    				return self.world[j][k]
    	return -1

if __name__ == "__main__":
    aworld = World(open("test_board.txt", "r"))
    print aworld.start
