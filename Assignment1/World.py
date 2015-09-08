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
        # self.start = getStart()
        # self.goal = getGoal()

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

if __name__ == "__main__":
    aworld = World(open("test_board.txt", "r"))
    for i in range(0, len(aworld.world)):
    	print aworld.world[i]
