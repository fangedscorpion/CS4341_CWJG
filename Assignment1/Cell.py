from Coord import Coord


class Cell:

    """Representation for world locations"""

    def __init__(self, coord, complexity):
        self.coord = coord
        self.vertDist = -1
        self.horizDist = -1
        self.isValid = False

        if(str(complexity).lower() == 'g'):
            self.isGoal = True
            self.isStart = False
            self.complexity = 1
            self.isValid = True
        elif(str(complexity).lower() == 's'):
            self.isStart = True
            self.isGoal = False
            self.complexity = 1
            self.isValid = True
        else:
            self.isStart = False
            self.isGoal = False
            self.complexity = int(complexity)
            if(not(complexity == -1)):
                self.isValid = True
            else:
                self.isValid = False

    # IN: -
    # OUT: returns Boolean if is the goal
    def getIsGoal(self):
        return self.isGoal

    # IN: -
    # OUT: returns Boolean if is the start
    def getIsStart(self):
        return self.isStart

    # IN: -
    # OUT: returns complexity (int -1, or 1 to 9)
    def getComplexity(self):
        return self.complexity

    # IN: -
    # OUT: returns the absolute coordinate of the cell (x, y pos)
    def getCoord(self):
        return self.coord

    # IN: -
    # OUT: returns horizontal distance to goal
    def getHorizDist(self):
        return self.horizDist

    # IN: -
    # OUT: returns vertical distance to goal
    def getVertDist(self):
        return self.vertDist

    def IsValid(self):
        return self.isValid

    # IN: complexity (integer 1 to 9)
    # OUT: -
    def setComplexity(self, newComplex):
        self.complexity = newComplex

    # IN: horizontal and vertical distance to goal (absolute) upper left if 0,0
    # OUT: -
    def setHorizVertDists(self, horiz, vert):
        self.horizDist = horiz
        self.vertDist = vert

    def __repr__(self):
        if(self.isValid):
            return ("CL:" + str(self.coord) +
                    "CM:" + str(self.complexity) +
                    "V,H:" + str(self.vertDist) +
                    "," + str(self.horizDist))
        else:
            return "NULL"

if __name__ == "__main__":
    coord = Coord(1, 1)
    complexity = 7
    horizDist = -1
    vertDist = -1

    testCell = Cell(coord, complexity)
    testCell.setHorizVertDists(horizDist, vertDist)

    print testCell
    assert testCell.IsValid() == True
    testCell2 = Cell(coord, -1)
    print testCell2
    assert testCell2.IsValid() == False
