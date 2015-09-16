

def geneticAlgorithm(puzzle):
	puzzle.initFirstGen()

	while(time ldakjflasdj):
		puzzle.EvalGen()
		puzzle.gen = Mate(puzzle.Gen)



def Mate(gen): #make the new generation, new Gen is not mutated or valid 
	#double check the ABOVE comment about mutation and validity
        tempGen = gen
	preGen = []

	while(tempGen != [])
		index1 = rand(0, len(tempGen)-1) 
		tempGen.remove(index1)
		chrome1 = tempGen[index1] 

		index2 = rand(0, len(tempGen)-1)
		tempGen.remove(index2)		
		chrome2 = tempGen[index2]

		index3 = rand(0, len(tempGen)-1)
		tempGen.remove(index3)		
		chrome3 = tempGen[index3]

		index4 = rand(0, len(tempGen)-1)
		tempGen.remove(index4)		
		chrome4 = tempGen[index4]

		if chrome1.fitness > chrome2.fitness:
			win1 = chrome1
			tempGen.append(chrome2)
		else:
			win1 = chrome2
			tempGen.append(chrome1)

		if chrome3.fitness > chrome4.fitness:
			win2 = chrome3
			tempGen.append(chrome4)
		else:
			win2 = chrome4
			tempGen.append(chrome3)

                #should we be adding to a compiled list of the entire generation or just take the 2 crossed over?
		preGen = crossOver(win1, win2)

	for chrome in preGen:
		chrome.mutate()
		chrome.makeValid() 

	return preGen


def mutate(gen):










