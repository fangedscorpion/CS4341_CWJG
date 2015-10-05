from Card.py import Card


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
				if card.hl == "high":
					handValue += 11
				else:
					handValue += 1
			elif card.isFaceCard():
				handValue += 10
			else:
				handValue += card.getValue()

	def showHiddenCards(self):
		for card in self.getCardList():
			card.setIsVisible(True)

	def popCard(self):
		if len(self.cardList) == 2:
			if self.cardList[0] = self.cardList[1]:
				popCard = self.cardList[1]
				self.cardList.remove(popCard)
				return popCard
			else:
				print "cards are not equal, cant be split"
		else:
			print "have more than 2 cards, cant split"

if __name__ == "__main__":
    a = Card(Card.ACE, Card.S, True)
    t = Card(2, Card.D, False)
    j = Card(Card.JACK, Card.S, True)
    q = Card(Card.QUEEN, Card.S, True)
    k = Card(Card.KING, Card.S, True)	

