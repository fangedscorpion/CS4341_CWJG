
class GameMove(object):
    topics = "won,loss,bust\n"

    def __init__(self):
    	self.won = 0
    	self.loss = 0
    	self.bust = 0

    def incWon(self):
    	self.won += 1

    def incLoss(self):
    	self.loss += 1

    def incBust(self):
    	self.bust += 1

    # Simple code
    def __repr__(self):
        return (str(self.won) + "," + str(self.loss) + "," + str(self.bust) + "\n")

if __name__ == '__main__':
    GameMove(1, 0, 0)
