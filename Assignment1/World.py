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
        (self.world, self.goal, self.start, self.rows,
         self.cols) = self.MakeWorld(self.file)
        self.world = self.UpdateGoalDists(
            self.world, self.rows, self.cols, self.goal)

    # INPUT: (World)
    # OUTPUT: (int, int) tuple of row, col bounds of World Cell Lists
    def GetBounds(self):
        return (self.rows, self.cols)

    # INPUT: (int) cols and (int) desired x
    # OUTPUT: (boolean) if the X pos is valid
    def IsXValid(self, xpos):
        return (xpos >= 0 and xpos < self.cols)

    # INPUT: (int) rows and (int) desired y
    # OUTPUT: (boolean) if the Y pos is valid
    def IsYValid(self, ypos):
        return (ypos >= 0 and ypos < self.rows)

    # INPUT: (Cell) current Cell (Cell) cell to compare direction (int) direction N,E,S,W (0,1,2,3)
    # OUTPUT: (boolean) if the cell is in the same direction
    def IsSameDirection(self, currentcell, acell, direction):
        coordcur = acell.getCoord()
        coordcurX = coordcur.getX()
        coordcurY = coordcur.getY()

        coord = acell.getCoord()
        coordX = coord.getX()
        coordY = coord.getY()

        if(direction == 0):
            # North
            return ((coordX == coordcurX) and (coordY <= coordcurY))
        elif(direction == 1):
            # East
            return ((coordX >= coordcurX) and (coordY == coordcurY))
        elif(direction == 2):
            # South
            return ((coordX == coordcurX) and (coordY >= coordcurY))
        elif(direction == 3):
            # West
            return ((coordX <= coordcurX) and (coordY == coordcurY))
        else:
            # Error
            return False

    # INPUT: (Cell) current pos, and (int) direction
    # OUTPUT: (boolean) representing if can bash in the given direction
    def CanBash(self, acell, direction):
        coord = acell.getCoord()
        coordX = coord.getX()
        coordY = coord.getY()

        if(direction == 0):
            # North
            return (self.IsYValid(coordY - 1))
        elif(direction == 1):
            # East
            return (self.IsXValid(coordX + 1))
        elif(direction == 2):
            # South
            return (self.IsYValid(coordY + 1))
        elif(direction == 3):
            # West
            return (self.IsXValid(coordX - 1))
        else:
            # Error
            return False

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
                # Get the start and goal while building the world
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
                horzDist = abs(
                    goalCoords.getX() - world[r][c].getCoord().getX())
                vertDist = abs(
                    goalCoords.getY() - world[r][c].getCoord().getY())
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
                if self.world[j][k].getIsStart():
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
                if self.world[j][k].getIsGoal:
                    return self.world[j][k]
        return -1

    # INPUT: (Cell) current cell
    # OUTPUT: -
    # Modifies the 8 cells around the given cell to have the new demo val
    def GetWrecked(self, acell):
        yohoodies = self.get8Neighbors(acell.getCoord())

        for bro in range(0, len(yohoodies)):
            if(yohoodies[bro].IsValid() and not yohoodies[bro].getIsStart() and not yohoodies[bro].getIsGoal()):
                yohoodies[bro].setComplexity(3)

    # returns a list of the 4 neighbors surrounding a given coordinate
    # [N, E, S, W]
    # INPUT -> (Coord) coordinate
    # OUTPUT -> (list of Cells) 4 neighbors
    def getNeighbors(self, a_coord):
        if(not self.IsYValid(a_coord.getY() - 1)):
            neighborN = Cell(Coord(-1, -1), -1)  # Null cell
        else:
            neighborN = self.world[a_coord.getY() - 1][a_coord.getX()]

        if(not self.IsXValid(a_coord.getX() + 1)):
            neighborE = Cell(Coord(-1, -1), -1)  # Null cell
        else:
            neighborE = self.world[a_coord.getY()][a_coord.getX() + 1]

        if(not self.IsXValid(a_coord.getX() - 1)):
            neighborW = Cell(Coord(-1, -1), -1)  # Null cell
        else:
            neighborW = self.world[a_coord.getY()][a_coord.getX() - 1]

        if(not self.IsYValid(a_coord.getY() + 1)):
            neighborS = Cell(Coord(-1, -1), -1)  # Null cell
        else:
            neighborS = self.world[a_coord.getY() + 1][a_coord.getX()]

        neighbors = [neighborN, neighborE, neighborS, neighborW]
        return neighbors

    # returns a list of the 4 bash neighbors surrounding a given coordinate
    # [N, E, S, W]
    # INPUT -> (Coord) coordinate
    # OUTPUT -> (list of Cells) 4 bash neighbors
    def getBashNeighbors(self, a_coord):
        if(not self.IsYValid(a_coord.getY() - 2)):
            neighborN = Cell(Coord(-1, -1), -1)  # Null cell
        else:
            neighborN = self.world[a_coord.getY() - 2][a_coord.getX()]

        if(not self.IsXValid(a_coord.getX() + 2)):
            neighborE = Cell(Coord(-1, -1), -1)  # Null cell
        else:
            neighborE = self.world[a_coord.getY()][a_coord.getX() + 2]

        if(not self.IsXValid(a_coord.getX() - 2)):
            neighborW = Cell(Coord(-1, -1), -1)  # Null cell
        else:
            neighborW = self.world[a_coord.getY()][a_coord.getX() - 2]

        if(not self.IsYValid(a_coord.getY() + 2)):
            neighborS = Cell(Coord(-1, -1), -1)  # Null cell
        else:
            neighborS = self.world[a_coord.getY() + 2][a_coord.getX()]

        neighbors = [neighborN, neighborE, neighborS, neighborW]
        return neighbors

    # returns a list of all 8 neighbors surrounding a given coordinate
    # [N, NE, E, SE, S, SW, W, NW]
    # INPUT -> (Coord) coordinate
    # OUTPUT -> (list of Cells) 8 neighbors
    def get8Neighbors(self, a_coord):
        (neighborN, neighborE, neighborS, neighborW) = self.getNeighbors(
            a_coord)

        # Logic here assumes grid is rectangular thankfully
        if(neighborN.IsValid() and neighborE.IsValid()):
            neighborNE = self.world[a_coord.getY() - 1][a_coord.getX() + 1]
        else:
            neighborNE = Cell(Coord(-1, -1), -1)  # Null cell

        if(neighborS.IsValid() and neighborE.IsValid()):
            neighborSE = self.world[a_coord.getY() + 1][a_coord.getX() + 1]
        else:
            neighborSE = Cell(Coord(-1, -1), -1)  # Null cell

        if(neighborW.IsValid() and neighborS.IsValid()):
            neighborSW = self.world[a_coord.getY() + 1][a_coord.getX() - 1]
        else:
            neighborSW = Cell(Coord(-1, -1), -1)  # Null cell

        if(neighborN.IsValid() and neighborW.IsValid()):
            neighborNW = self.world[a_coord.getY() - 1][a_coord.getX() - 1]
        else:
            neighborNW = Cell(Coord(-1, -1), -1)  # Null cell

        neighbors = [neighborN, neighborNE, neighborE, neighborSE,
                     neighborS, neighborSW, neighborW, neighborNW]
        return neighbors

if __name__ == "__main__":
    aworld = World(open("test_board.txt", "r"))

    bn = aworld.getBashNeighbors(Coord(1, 1))
    for b in bn:
        print b

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
    # testCoord = Coord(0,0)

    # print testCoord
    # neibs = aworld.get8Neighbors(testCoord)
    # print neibs, "\n"

    # testCoord = Coord(0,1)
    # print testCoord
    # neibs = aworld.get8Neighbors(testCoord)
    # print neibs, "\n"

    # testCoord = Coord(1,1)
    # print testCoord
    # neibs = aworld.get8Neighbors(testCoord)
    # print neibs, "\n"

    # testCoord = Coord(3, 2)
    # print testCoord
    # neibs = aworld.get8Neighbors(testCoord)
    # print neibs, "\n"
    ######
    # for k in range(0, aworld.rows):
    #     for l in range(0, aworld.cols):
    # print aworld.getCell(Coord(l, k))
    #         cell = aworld.getCell(Coord(l,k))
    #         if(aworld.getCell(Coord(l,k)).getIsGoal()):
    #             print "G", "\t",
    #         elif(aworld.getCell(Coord(l,k)).getIsStart()):
    #             print "S", "\t",
    #         else:
    #             print aworld.getCell(Coord(l,k)).getComplexity(),"\t",
    #     print "\n"

    # aworld.GetWrecked(aworld.getCell(Coord(1,1)))
    # print
    # print

    # for k in range(0, aworld.rows):
    #     for l in range(0, aworld.cols):
    # print aworld.getCell(Coord(l, k))
    #         cell = aworld.getCell(Coord(l,k))
    #         if(aworld.getCell(Coord(l,k)).getIsGoal()):
    #             print "G", "\t",
    #         elif(aworld.getCell(Coord(l,k)).getIsStart()):
    #             print "S", "\t",
    #         else:
    #             print aworld.getCell(Coord(l,k)).getComplexity(),"\t",
    #     print "\n"
