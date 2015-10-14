import pickle
import os



if __name__ == '__main__':
    fullListOfDir = os.listdir(os.path.curdir)

    dictsOnly = []
    for fileName in fullListOfDir:
        if(fileName.endswith(".p")):
            dictsOnly.append(fileName)

    print dictsOnly

    firstDir = pickle.load(open(dictsOnly[0], "rb"))

    for x in range(1, len(dictsOnly)):
        fileName = dictsOnly[x]

        print "FILE: ", fileName

        #open the dict
        tmpDic = pickle.load(open(fileName, "rb"))

        #update the dict
        for x in tmpDic.items():

            keyVal = x[0]
            value = x[1]
            if(firstDir.has_key(keyVal)):
                firstDir[keyVal] = (firstDir[keyVal][0] + tmpDic[keyVal][0],
                                    firstDir[keyVal][1] + tmpDic[keyVal][1],
                                    firstDir[keyVal][2] + tmpDic[keyVal][2])
            else:
                firstDir[keyVal] = tmpDic[keyVal]


    print firstDir
    pickle.dump(firstDir, open("MEGA_DICT.bin", "wb"))    




        

