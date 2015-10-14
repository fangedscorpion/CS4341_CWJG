
class GameMove(object):
    topics = "won,loss,bust\n"

    def __init__(self, won, loss, bust):
        self.won = won
        self.loss = loss
        self.bust = bust

    # Simple code
    def __repr__(self):
        return (str(self.won) + "," + str(self.loss) + "," + str(self.bust) + "\n")

if __name__ == '__main__':
    GameMove(1, 0, 0)
