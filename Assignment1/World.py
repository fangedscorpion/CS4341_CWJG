""" World Class """
""" Representation of all cells in the World """
from Coord import Coord
from Cell import Cell

class World(object):
    # file is the input world file
    # MakeWorld parses the input file and creates a list of a list of cells
    # self.start stores the starting cell to avoid using the function getStart() repeatidly
    # self.goal stores the goal cell to avoid using the function getGoal()
    # repeatidly

    def __init__(self, file):
        self.file = file
        (self.world, self.goal, self.start, self.rows, self.cols) = self.MakeWorld(self.file)
        self.world = self.UpdateGoalDists(self.world, self.rows, self.cols, self.goal)

    # INPUT: (World) 
    # OUTPUT: (int, int) tuple of row, col bounds of World Cell Lists
    def GetBounds(self):
        return (self.rows, self.cols)        

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

        goalCoords = -1
        startCoords = -1
        # assign values from lines into world list
        for k in range(0, len(lines)):
            for l in range(0, len(lines[k])):
                #Get the start and goal while building the world
                if(str(lines[k][l]).lower() == 'g'):
                    goalCoords = Coord(l, k)
                if(str(lines[k][l]).lower() == 's'):
                    startCoords = Coord(l, k)

                world[k][l] = Cell(Coord(l, k), lines[k][l])

        # Return a tuple of all important info
        return (world, goalCoords, startCoords, len(lines), len(lines[0]))

    # Updates info to get to the goal
    # INPUT: World object
    # OUTPUT: list of Cell
    def UpdateGoalDists(self, world, rows, cols, goalCoords):
        for r in range(0, rows):
            for c in range(0, cols):
                horzDist = abs(goalCoords.getX() - world[r][c].getCoord().getX())
                vertDist = abs(goalCoords.getY()- world[r][c].getCoord().getY())
                world[r][c].setHorizVertDists(horzDist, vertDist)
        return world

    # returns a Cell at a given coord
    # INPUT -> (Coord) coordinate
    # OUTPUT -> (Cell) a cell
    def getCell(self, a_coord):
        return self.world[a_coord.getY()][a_coord.getX()]

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

    # parses through world looking for the goal cell
    # if no starting cell is found, returns -1
    # INPUT -> none
    # OUTPUT -> (cell) starting cell, OR (int) -1
    def getGoal(self):
        for j in range(0, len(self.world)):
            for k in range(0, len(self.world[j])):
                # if self.world[j][k].isGoal():
                # ^ switch boolean line when Cell is defined
                if self.world[j][k] == "G":
                    return self.world[j][k]
        return -1

    # returns a list of the 4 neighbors surrounding a given coordinate
    # [N, E, S, W]
    # INPUT -> (Coord) coordinate
    # OUTPUT -> (list of Cells) 4 neighbors
    def getNeighbors(self, a_coord):
        if(a_coord.getY() - 1 < 0):
            neighborN = Cell(Coord(-1, -1), -1) # Null cell
        else:
            neighborN = self.world[a_coord.getY() - 1][a_coord.getX()]
        
        if(a_coord.getX() + 1 == self.cols):
            neighborE = Cell(Coord(-1, -1), -1) # Null cell
        else:
            neighborE = self.world[a_coord.getY()][a_coord.getX() + 1]
       
        if(a_coord.getX() - 1 < 0):
            neighborW = Cell(Coord(-1, -1), -1) # Null cell
        else:
            neighborW = self.world[a_coord.getY()][a_coord.getX() - 1]
        
        if(a_coord.getY() + 1 == self.rows):
            neighborS = Cell(Coord(-1, -1), -1) # Null cell
        else:
            neighborS = self.world[a_coord.getY() + 1][a_coord.getX()]
        
        neighbors = [neighborN, neighborE, neighborS, neighborW]
        return neighbors

    # returns a list of all 8 neighbors surrounding a given coordinate
    # [N, NE, E, SE, S, SW, W, NW]
    # INPUT -> (Coord) coordinate
    # OUTPUT -> (list of Cells) 8 neighbors
    def get8Neighbors(self, a_coord):
        (neighborN, neighborE, neighborS, neighborW) = self.getNeighbors(a_coord)

        #Logic here assumes grid is rectangular thankfully
        if(neighborN.IsValid() and neighborE.IsValid()):
            neighborNE = self.world[a_coord.getY() - 1][a_coord.getX() + 1]
        else:
            neighborNE = Cell(Coord(-1, -1), -1) # Null cell
        
        if(neighborS.IsValid() and neighborE.IsValid()):
            neighborSE = self.world[a_coord.getY() + 1][a_coord.getX() + 1]
        else:
            neighborSE = Cell(Coord(-1, -1), -1) # Null cell

        if(neighborW.IsValid() and neighborS.IsValid()):
            neighborSW = self.world[a_coord.getY() + 1][a_coord.getX() - 1]
        else:
            neighborSW = Cell(Coord(-1, -1), -1) # Null cell

        if(neighborN.IsValid() and neighborW.IsValid()):
            neighborNW = self.world[a_coord.getY() - 1][a_coord.getX() - 1]
        else:
            neighborNW = Cell(Coord(-1, -1), -1) # Null cell        
   
        neighbors = [neighborN, neighborNE, neighborE, neighborSE,
                     neighborS, neighborSW, neighborW, neighborNW]
        return neighbors

if __name__ == "__main__":
    aworld = World(open("test_board.txt", "r"))

    # Test neighbors
    # testCoord = Coord(0,0)

    # neibs = aworld.getNeighbors(testCoord)
    # print neibs

    # testCoord = Coord(0,1)

    # neibs = aworld.getNeighbors(testCoord)
    # print neibs

    # testCoord = Coord(1,1)

    # neibs = aworld.getNeighbors(testCoord)
    # print neibs

    # testCoord = Coord(3, 2)

    # neibs = aworld.getNeighbors(testCoord)
    # print neibs
    ######

    # Test get8Neighbors
    testCoord = Coord(0,0)

    print testCoord
    neibs = aworld.get8Neighbors(testCoord)
    print neibs, "\n"

    testCoord = Coord(0,1)
    print testCoord
    neibs = aworld.get8Neighbors(testCoord)
    print neibs, "\n"

    testCoord = Coord(1,1)
    print testCoord
    neibs = aworld.get8Neighbors(testCoord)
    print neibs, "\n"

    testCoord = Coord(3, 2)
    print testCoord
    neibs = aworld.get8Neighbors(testCoord)
    print neibs, "\n"
    ######



    for k in range(0, aworld.rows):
        for l in range(0, aworld.cols):
            #print aworld.getCell(Coord(l, k))
            cell = aworld.getCell(Coord(l,k))
            if(aworld.getCell(Coord(l,k)).getIsGoal()):
                print "G", "\t",
            elif(aworld.getCell(Coord(l,k)).getIsStart()):
                print "S", "\t",
            else:
                print aworld.getCell(Coord(l,k)).getComplexity(),"\t",
        print "\n"    
