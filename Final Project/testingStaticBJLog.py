from Move import Move
from DealerMove import DealerMove
from StaticBJLogger import StaticBJLogger

aMove = Move(10, "Hit", 0, 0)
aMove2 = Move(19, "Stay", 0, 0)
aMove3 = Move(18, "Hit", 1, 0)
aMove4 = Move(18, "Split", 0, 2)  # Breaks into two hands being played

aDMove = DealerMove(10, -1)
aDMove2 = DealerMove(16, 1)
aDMove3 = DealerMove(22, 0)

playerMoves = [aMove, aMove2, aMove3]
dealerMoves = [aDMove, aDMove2, aDMove3]

print "*" * 50
print "Testing StaticBJLogger"
StaticBJLogger.init(1)  # MUST CALL THIS FIRST

for i in range(0, len(playerMoves)):
    StaticBJLogger.writePlayerMove(playerMoves[i])
    StaticBJLogger.writeDealerMove(dealerMoves[i])
