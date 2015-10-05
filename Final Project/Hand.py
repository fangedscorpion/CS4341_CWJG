
class Hand(object):

	def __init__(self, cardList):
		self.cardList = cardList #the list of cards in a player's hand

	# overriding the equals (==) operator

	def __eq__(self, other):
		return self.cardList == other.cardList


	def __ne__(self, other):
		return not self == other

	def __repr__(self):
		return "Hand:" + str(self.cardList)

	# input: -
	# output: returns the cardList of a hand
	def getCardList(self):
		return self.cardList

	# input: a card to add to the hand
	# output: -
	def addCard(self, newCard):
		self.cardList.append(newCard)

	def getHandValue(self):
		handValue = 0
		for card in self.cardList:
			if card.isAce():
				if card
