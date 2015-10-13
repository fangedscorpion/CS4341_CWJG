""" This class is to hold and calculate all values assosiated with card counting. """


class CC(object):
    cardsPerSuit = 4    # the number of cards in each suit
    groupSize = 4   # the number of card values which all result in 10
    groupValue = 10  # the value of the cards in the larger group
    categories = 11  # the number of distinct card values

    def __init__(self, numDecks):
        self.numDecks = numDecks
        self.suitTotal = numDecks * CC.cardsPerSuit
        self.count = [0] * CC.categories

    # updates the counted list for the new card value
    # the input is the card value
    def update(self, value):
        if value > CC.groupValue:
            value = CC.groupValue
        self.count[value] += 1

    # returns a new list, equal to self.count for all the values 1 minus
    # it is expected that the first element is 0 and does not count
    def oneMinus(self):
        mod = [0] * len(self.count)

        for j in range(1, len(self.count)):
            mod[j] = 1 - self.count[j]

        return mod

    # calculates the un-normalized value of all the count values
    # uses input_, which is all of the count values from self.count 1 minus
    # it is expected that the first element is 0 and does not count
    def getCurStat(self, input_):
        stats = [0] * len(input_)

        for j in range(1, len(input_)):
            if j == CC.groupValue:
                stats[j] = input_[j] / \
                    (float(CC.cardsPerSuit * self.numDecks * CC.groupSize))

            else:
                stats[j] = input_[j] / \
                    (float(CC.cardsPerSuit * self.numDecks))

        return stats

    # normalizes all values in input_
    # returns a normalized list
    # it is expected that the first element is 0 and does not count
    def normalize(self, input_):
        alpha = float(sum(input_))

        norm = [0] * len(input_)

        for j in range(1, len(input_)):
            norm[j] = input_[j] / alpha

        return norm

    # returns the expected value
    # it is expected that the first element is 0 and does not count
    def EV(self, input_):
        exVal = 0
        for j in range(1, len(input_)):
            exVal += (j * input_[j])

        return exVal

    # returns the expected value to be delt by the deck
    # the value is calculated with the expected value formula
    # the value returned is the value calculated, not a discrete card value
    def getEV(self):
        oneMin = self.oneMinus()
        stat = self.getCurStat(oneMin)
        norm = self.normalize(stat)
        return self.EV(norm)

if __name__ == "__main__":
    inputs = [0.5] * 11
    inputs[0] = 0
    alpha = CC(6)
    alpha.normalize(inputs)
    print alpha.EV([0, 0.68, 0.5])
