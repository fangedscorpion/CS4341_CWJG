from Action import Action

class Bash(Action):

	"""Class for the Bash Action"""

	def __init__(self):
		Action.__init__(self, "Bash", 3)

if __name__ == "__main__":
    abash = Bash()
    assert "Name: Bash. Cost: 3" == str(abash) 
    assert abash.getTimeCost() == 3