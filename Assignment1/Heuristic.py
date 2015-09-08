""" Class for Heuristic functions """
from Coord import Coord


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
        # return min(a_cell.horz, a_cell.vert)
        return min(1, 3)

    # This function returns the heuristic evaluation for heuristic 3
    # This function chooses the maximum between a cell's horz. and vert. distances to the goal
    # INPUT -> (Cell) the cell being evaluated
    # OUTPUT -> (int) heuristic calculaton
    def heur3(self, a_cell):
        # return max(a_cell.horz, a_cell.vert)
        return max(1, 3)

    # This function returns the heuristic evaluation for heuristic 4
    # This function returns the sum of a cell's horz. and vert. distances to the goal
    # INPUT -> (Cell) the cell being evaluated
    # OUTPUT -> (int) heuristic calculaton
    def heur4(self, a_cell):
        # return max(a_cell.horz, a_cell.vert)
        return 1 + 3

if __name__ == "__main__":
    a_h = Heuristic(4, Coord(1, 2))
    print a_h.heur4("test cell")
