class Piece:

    # pieceType is a string (door, wall, lookout)
    # width is a number (float or int)
    # strength is a number (float or int) # of pieces can be stacked on
    # cost is expense of piece (number float or int)
    def __init__(self, pieceType, width, strength, cost, ID):
        self.type = pieceType
        self.width = width
        self.strength = strength
        self.cost = cost
        self.ID = ID

    def __repr__(self):
        return (str(self.type) + "," + str(self.width) + "," + str(self.strength) +
                "," + str(self.cost) + "," + str(self.ID))

    def __eq__(self, other):
        return (self.type.lower() == other.getType().lower() and
                self.width == other.getWidth() and
                self.strength == other.getStrength() and
                self.cost == other.getCost() and self.ID == other.getID())

    def getCost(self):
        return self.cost

    def getID(self):
        return self.ID

    def canFit(self, other):
        return self.width <= other.getWidth()

    def canSupportNum(self, numPieces):
        return self.strength >= numPieces

    def getStrength(self):
        return self.strength

    def getType(self):
        return self.type

    def getWidth(self):
        return self.width

    def isDoor(self):
        return self.type.lower() == "door"

    def isLookout(self):
        return self.type.lower() == "lookout"

    def isWall(self):
        return self.type.lower() == "wall"

    def getDictKey(self):
        # unhashable otherwise
        return (self.type[0] + str(self.width) + str(self.strength) + str(self.cost))

if __name__ == '__main__':
    d1 = Piece("Door", 5, 3, 2, 0)
    w1 = Piece("Wall", 5, 5, 1, 1)
    w2 = Piece("Wall", 4, 3, 1, 2)
    d2 = Piece("Door", 3, 5, 2, 3)
    w3 = Piece("Wall", 3, 3, 2, 4)
    l1 = Piece("Lookout", 2, 2, 3, 5)
    l2 = Piece("Lookout", 3, 1, 2, 6)
    l3 = Piece("Lookout", 3, 1, 2, 6)

    assert d1.isLookout() == False
    assert l1.isLookout() == True
    assert d1.isDoor() == True
    assert w1.isDoor() == False

    assert l2 != l1
    assert l3 == l2

    piecesList = [d1, w1, w2, d2, w3, l1, l2]

    for piece in piecesList:
        print piece
