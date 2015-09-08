class Node:
	"""This is the class the represents the node of a path. This is like a path segment essentially"""
	
	def __init__(self, cell, actionList):
		self.currentCell = cell
		self.actionList = actionList

	def getActionList(self):
		return self.actionList

	def getParent(self):
		return self.parent

	def getCurrentCell(self):
		return self.currentCell



if __name__ == "__main__":
	a_node = Node("cell", ["turn"])
	print a_node.getActionList(), a_node.getCurrentCell()
	print "['turn']", "cell"