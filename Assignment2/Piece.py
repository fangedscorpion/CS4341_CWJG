class Piece:

	# pieceType is a string (door, wall, lookout)
	# width is a number (float or int)
	# strength is a number (float or int) # of pieces can be stacked on
	# cost is expense of piece (number float or int)
	def __init__(self, pieceType, width, strength, cost):
		self.type = pieceType 
		self.width = width
		self.strength = strength
		self.cost = cost

	def __repr__(self):
		return (str(self.type) + "," + str(self.width) + "," + str(self.strength) + \
			"," + str(self.cost))

	def getCost(self):
		return self.cost

	def getStrength(self):
		return self.strength

	def getType(self):
		return self.type

	def getWidth(self):
		return self.width

	def getDictKey(self):
		return (self.type[0]+str(self.width)+str(self.strength)+str(self.cost))

if __name__ == '__main__':
	d1 = Piece("Door", 5,3,2)
	w1 = Piece("Wall", 5,5,1)
	w2 = Piece("Wall", 4,3,1)
	d2 = Piece("Door", 3,5,2)
	w3 = Piece("Wall", 3,3,2)
	l1 = Piece("Lookout",2,2,3)
	l2 = Piece("Lookout",3,1,2)

	piecesList = [d1, w1, w2, d2, w3, l1, l2]

	for piece in piecesList:
		print piece