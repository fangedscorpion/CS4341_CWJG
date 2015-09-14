import time

def geneticAlgo(lon, allowedTime, dictionary): #lon = list of numbers
    #timeRef = time.clock() # This will be a fractional number 
    timeRef = time.time() #This seemed like a better timer thing --> more usable
    popSize = 500
    masterDict = dictionary
    parents = createParents(lon, popSize)

    while time.time() <= timeRef + allowedTime:
        #makeMatingPool(parents)
        print "HALP"


# def makeMasterDict(lon):
#     masterDict = []
#     tempLon = lon
#     for each in tempLon: # for each number in the list
#         numOfEach = 1 # the number of each starts at 1
#         tempLon.remove(each): # remove each from the list
#         for dups in tempLon # look for duplicates of each
#             if each == dups: # if duplicate found, remove
#                 tempLon.remove(dups)
#                 numOfEach += 1
#         masterDict[each] = numOfEach

#     return masterDict  


def makeMatingPool(parents):
    for parentA in parents:
        parentB = parents[random.random(0,(len(parents)-1))]
        if parentA.fitness > parentB.fitness:
            print "Parent A better"
            

def createParents(lon, popSize):
    for i in range (popSize):
        print i
        

    return "Something useful"


