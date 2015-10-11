from Card import Card

alist = [Card(4, 2, True), Card(3, 4, True)]

for alpha in alist:
	if alpha.getValue() == 4:
		alist.append(alist.pop(1))
	print alpha