import unittest
from Chromosome1 import *
from Puzzle1 import *

class tests(unittest.TestCase):
    def test_chromeList(self):
        tchrom = chromosome1([1, 2, 3])
        self.assertEqual(tchrom.lon, [1, 2, 3])

    def test_fitness(self):
        tchrom = chromosome1([1, 2, 3])
        self.assertEqual(tchrom.fitness(), 6)

    def test_crossoverIsh(self):
        #tests how crossover works, but does not run the actual function to get rid of randomization for simplicity in testing
        tchrom = chromosome1([1, 2, 3, 4, 5, 6]) #parent
        rchrom = chromosome1([7, 8, 9, 10, 11, 12, 13]) #parent
        split1 = 2 #set split values to check functionality
        split2 = 4 #set split values to check functionality
        
        clon = tchrom.lon[0:split1] + rchrom.lon[split2:len(rchrom.lon)]
        klon = rchrom.lon[0:split2] + tchrom.lon[split1:len(tchrom.lon)]

        cchrom = chromosome1(clon) #child
        kchrom = chromosome1(klon) #child
        self.assertEqual(cchrom.lon, [1, 2, 11, 12, 13])
        self.assertEqual(kchrom.lon, [7, 8, 9, 10, 3, 4, 5, 6])

    def test_isValid(self):
        master = {1:1, 2:1, 3:1, 4:1, 5:1}
        tchrom = chromosome1([1, 2, 3, 3, 4, 5, 6])
        self.assertEqual(tchrom.isValid(3, master), False)
        self.assertEqual(tchrom.isValid(1, master), True)

    def test_fixChild(self):
        master = {1:1, 2:1, 3:1, 4:1, 5:2}
        tchrom = chromosome1([1, 2, 2, 3, 5])
        tchrom.fixChild(master)
        result = True
        for i in range(0, len(tchrom.lon) - 1):
            if(not tchrom.isValid(tchrom.lon[i], master)):
                result = False
        self.assertEqual(result, False)


if __name__ == "__main__":
    unittest.main()

