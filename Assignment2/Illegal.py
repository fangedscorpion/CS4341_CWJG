""" This class is to hold information on the analysis of an illegal Chromosome """
""" The design of the object is to built up after initialization, not built all at once """

class Illegal(object):

    # self.value = the value being represented that causes illeglaity
    # self.count = the number of times self.value is represented in the Chromosome
    # self.locations = a list of the locations in which self.value is
    # represented
    def __init__(self, val, count, locations):
        self.value = val
        self.count = count
        self.locations = locations

    # This function sets self.value
    # INPUT -> new value
    # OUTPUT -> none
    def setValue(self, val):
        self.value = val

    # This function gets self.value
    # INPUT -> none
    # OUTPUT -> self.value
    def getValue(self):
        return self.value

    # This function sets self.count
    # INPUT -> new count
    # OUTPUT -> none
    def setCount(self, cou):
        self.count = cou

    # This function increments self.count
    # INPUT -> none
    # OUTPUT -> new count
    def incCount(self):
        self.count += 1
        return self.count

    # This function returns self.count
    # INPUT -> none
    # OUTPUT -> self.count
    def getCount(self):
        return self.count

    # This function adds a new location to self.location
    # INPUT -> location
    # OUTPUT -> none
    def addLocation(self, loc):
        self.locations.append(loc)

    # This function retuns the list of locations
    # INPUT -> none
    # OUTPUT -> (list) self.locations
    def getLocations(self):
        return self.locations

    def __repr__(self):
        return ("Val: " + str(self.value) + ", Count: " + str(self.count) + ", Locs: " + str(self.locations))


if __name__ == "__main__":
    ill = Illegal()
    print ill
    print

    ill.setValue(3)
    print "val: ", ill.getValue(), "3"
    print

    ill.setCount(1)
    print "count: ", ill.getCount(), 1
    ill.incCount()
    print "count: ", ill.getCount(), 2
    print

    ill.addLocation((1, 3))
    ill.addLocation((2, 4))
    print ill.getLocations(), [(1, 3), (2, 4)]
