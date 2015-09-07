class Node:
	"""This is the class the represents the node of a path. This is like a path segment essentially"""
	currentCell #This is the cell that is associated with the Node
	actionList #This is a list of Actions that was taken to get to the current cell from the previous Node

	def __init__(self, cell, actionList):
		self.currentCell = cell
		self.actionList = actionList

	def getActionList(self):
		return self.actionList

	def getParent(self):
		return self.parent

	def getCurrentCell(self):
		return self.currentCell



if "__name__" == "__main__":
	self.currentCell = Cell()
	self.actionList = list(TurnAction())
	print self