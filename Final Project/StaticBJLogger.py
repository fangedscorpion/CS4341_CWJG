
class StaticBJLogger(object):

    fileIndex = 1
    fileNamePrefix = "BJstats_"
    fileNameSuffix = ".txt"
    fileNameCurrent = fileNamePrefix + str(fileIndex) + fileNameSuffix

    @staticmethod
    def init(num):
        StaticBJLogger.fileNameCurrent = StaticBJLogger.fileNamePrefix + \
            str(num) + StaticBJLogger.fileNameSuffix
        fileHandleCurrent = open(StaticBJLogger.fileNameCurrent, "w")
        fileHandleCurrent.close()

    @staticmethod
    def writePlayerMove(moveObj):
        fileHandleCurrent = open(StaticBJLogger.fileNameCurrent, "a")
        fileHandleCurrent.write(str(moveObj))  # See the Move.py class
        fileHandleCurrent.close()

    @staticmethod  # needs this identifier to be called from the class
    def writeDealerMove(moveObj):
        fileHandleCurrent = open(StaticBJLogger.fileNameCurrent, "a")
        fileHandleCurrent.write(str(moveObj))  # See the Move.py class
        fileHandleCurrent.write("\n")
        fileHandleCurrent.close()
