import time

def geneticAlgo(lon, allowedTime): #loe = list of numbers
    timeRef = time.clock()
    popSize = 500
    masterDict = makeMasterDict(lon)
    parents = createParents(lon, popSize)

    while timeRef + allowedTime <= time.clock():
        makeMatingPool(parents)








def makeMasterDict(lon):
    masterDict = []
    tempLon = lon
    for each in tempLon: # for each number in the list
        numOfEach = 1 # the number of each starts at 1
        tempLon.remove(each): # remove each from the list
        for dups in tempLon # look for duplicates of each
            if each == dups: # if duplicate found, remove
                tempLon.remove(dups)
                numOfEach += 1
        masterDict[each] = numOfEach

    return masterDict  


def makeMatingPool(parents):
    for parentA in parents:
        parentB = parents[random.random(0,(len(parents)-1))]
        if parentA.fitness > parentB.fitness:
            

def createParents(lon, popSize):
    for i in range (popSize):

        return listofParents


