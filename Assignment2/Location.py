class Location():	
	def __init__(self, binNum, indexInBin):
		self.binNum = binNum
		self.indexInBin = indexInBin

	def getBin(self):
		return self.binNum

	def getIndex(self):
		return self.indexInBin

	def __repr__(self):
		return "(" + str(self.binNum) + " , " + str(self.indexInBin) + ")"