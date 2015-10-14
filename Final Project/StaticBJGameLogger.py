from GameMove import GameMove

class StaticBJGameLogger(object):

    fileIndex = 1
    BSfileNamePrefix = "statsBS_"
    ROfileNamePrefix = "statsRO_"
    CCfileNamePrefix = "statsCC_"
    fileNameSuffix = ".csv"
    BSfileName = BSfileNamePrefix + fileNameSuffix
    ROfileName = ROfileNamePrefix + fileNameSuffix
    CCfileName = CCfileNamePrefix + fileNameSuffix

    @staticmethod
    def init(num):
        StaticBJGameLogger.BSfileName = StaticBJGameLogger.BSfileNamePrefix + str(num) + StaticBJGameLogger.fileNameSuffix
        StaticBJGameLogger.ROfileName = StaticBJGameLogger.ROfileNamePrefix + str(num) + StaticBJGameLogger.fileNameSuffix
        StaticBJGameLogger.CCfileName = StaticBJGameLogger.CCfileNamePrefix + str(num) + StaticBJGameLogger.fileNameSuffix

        fileHandleCurrent = open(StaticBJGameLogger.BSfileName, "w")
        fileHandleCurrent.write(GameMove.topics)
        fileHandleCurrent.close()

        fileHandleCurrent = open(StaticBJGameLogger.ROfileName, "w")
        fileHandleCurrent.write(GameMove.topics)
        fileHandleCurrent.close()

        fileHandleCurrent = open(StaticBJGameLogger.CCfileName, "w")
        fileHandleCurrent.write(GameMove.topics)
        fileHandleCurrent.close()

    @staticmethod
    def writeBSMove(moveObj):
        fileHandleCurrent = open(StaticBJGameLogger.BSfileName, "a")
        fileHandleCurrent.write(str(moveObj))  # See the GameMove.py class
        fileHandleCurrent.close()

    @staticmethod
    def writeROMove(moveObj):
        fileHandleCurrent = open(StaticBJGameLogger.ROfileName, "a")
        fileHandleCurrent.write(str(moveObj))  # See the GameMove.py class
        fileHandleCurrent.close()

    @staticmethod
    def writeCCMove(moveObj):
        fileHandleCurrent = open(StaticBJGameLogger.CCfileName, "a")
        fileHandleCurrent.write(str(moveObj))  # See the GameMove.py class
        fileHandleCurrent.close()

if __name__ == "__main__":
    StaticBJGameLogger.init(0)
    StaticBJGameLogger.writeBSMove(GameMove(0,0,2))
    StaticBJGameLogger.writeROMove(GameMove(1,0,0))
    StaticBJGameLogger.writeCCMove(GameMove(0,2,0))
