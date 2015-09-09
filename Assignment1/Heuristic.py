""" Class for Heuristic functions """
from Coord import Coord
from Cell import Cell

class Heuristic(object):
    # function is an integer representing the specific huersitic function
    # gCoord is the coordinate of the goal

    def __init__(self, function, gCoord):
        self.function = function
        self.gCoord = gCoord

    # This function returns the integer representing the specific heuristic function
    # INPUT -> none
    # OUTPUT -> (int) function
    def getFunction(self):
        return self.function

    # This function returns the heuristic evaluation for heuristic 1
    # heuristic 1 is always 0
    # INPUT -> (Cell) the cell being evaluated
    # OUTPUT -> (int) 0
    def heur1(self, a_cell):
        return 0

    # This function returns the heuristic evaluation for heuristic 2
    # This function chooses the minimum between a cell's horz. and vert. distances to the goal
    # INPUT -> (Cell) the cell being evaluated
    # OUTPUT -> (int) heuristic calculaton
    def heur2(self, a_cell):
        return min(a_cell.getHorizDist(), a_cell.getVertDist())

    # This function returns the heuristic evaluation for heuristic 3
    # This function chooses the maximum between a cell's horz. and vert. distances to the goal
    # INPUT -> (Cell) the cell being evaluated
    # OUTPUT -> (int) heuristic calculaton
    def heur3(self, a_cell):
        return max(a_cell.getHorizDist(), a_cell.getVertDist())

    # This function returns the heuristic evaluation for heuristic 4
    # This function returns the sum of a cell's horz. and vert. distances to the goal
    # INPUT -> (Cell) the cell being evaluated
    # OUTPUT -> (int) heuristic calculaton
    def heur4(self, a_cell):
        return a_cell.getHorizDist() + a_cell.getVertDist()

    # This function returns the heuristic evaluation for heuristic 5
    # For this function, if the cell is not in the same row or column as the goal, it returns heur4 + 1 (a cost of turning)
    # Otherwise, it returns heur4
    # INPUT -> (Cell) the cell being evaluated
    # OUTPUT -> (int) heuristic calculaton
    def heur5(self, a_cell):
        if (a_cell.getHorizDist() != 0) and (a_cell.getVertDist() != 0):
            return self.heur4(a_cell) + 1
        else:
            return self.heur4(a_cell)

    # This function returns the heuristic evaluation for heuristic 6
    # This function returns a non-admissable heuristic, heur5 * 3
    # INPUT -> (Cell) the cell being evaluated
    # OUTPUT -> (int) heuristic calculaton
    def heur6(self, a_cell):
        return self.heur5(a_cell) * 3

if __name__ == "__main__":
    testCoord = Coord(1, 2)
    a_h = Heuristic(4, testCoord)
    cell = Cell(testCoord, 8)
    cell.setHorizVertDists(2, 1) # Horiz, vert
    print "Actual: ",a_h.heur5(cell), "Test: ", 4
    print "Actual: ",a_h.heur6(cell), "Test: ", 12
    print "Actual: ",a_h.heur4(cell), "Test: ", 3
    print "Actual: ",a_h.heur3(cell), "Test: ", 2
    print "Actual: ",a_h.heur2(cell), "Test: ", 1
    print "Actual: ",a_h.heur1(cell), "Test: ", 0
