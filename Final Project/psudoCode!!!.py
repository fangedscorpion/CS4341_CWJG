for i in range(players)	
	for h in range(players[i].hands):
		while keep_going:
			keep_going = players[i].playFunction()
