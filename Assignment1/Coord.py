""" A coordinate class """
class Coord(object):
	def __init__(self, x, y):
		self.x = x # the x coordinate value
		self.y = y # the y coordinate value

	# overriding the equals (==) operator
	def __eq__(self, other):
		return (self.x == other.x) and (self.y == other.y)

	# overriding the not equals (!=) operator
	def __ne__(self, other):
		return not self == other

	# returns the x coordinate
	def getX(self):
		return self.x

	# returns the y coordinate
	def getY(self):
		return self.y

if __name__ == "__main__":
	A = Coord(1,2)
	B = Coord(2,1)
	C = Coord(1,2)

	print A == B, "False"
	print A != B, "True"
	print A == C, "True"

	print A.getX(), "1"
	print A.getY(), "2"