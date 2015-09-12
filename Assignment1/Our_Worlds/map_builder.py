import sys
from random import randint

fileNum = sys.argv[1]
file = open("world1_" + fileNum + ".txt", "w+")

row = int(sys.argv[2])
col = int(sys.argv[3])

world = [[0 for x in range(col)] for x in range(row)]

for x in range(0, row):
	for y in range(0, col):
		world[x][y] = str(randint(1,9))

tenR = int(row * 0.1)
tenC = int(col * 0.1)
ninC = int(col * 0.9)
ninR = int(row * 0.9)

start = [randint(0, tenR), randint(0, tenC)]
goal = [randint(ninR, row-1), randint(ninC, col-1)]

world[start[0]][start[1]] = "S"
print world[start[0]][start[1]], "S"
world[goal[0]][goal[1]] = "G"
print start, goal
for x in range(0, row):
	for y in range(0, col):
		file.write(world[x][y])
		file.write("\t")
	file.write("\n")
