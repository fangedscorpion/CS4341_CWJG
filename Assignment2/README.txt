To run:

$python ga.py filename.txt puzzleNum secondsToRun
For puzzle 3, it is suggested to let the function run for at least 30 seconds. Less time than that and it will arrive at an answer, but not as good of an answer as it could.

The mutation rate and population size are in ga.py on lines {21, 22}, respectively

In the file ga.py, there is a variable "debug_mode" on line 6.
When debug_mode is set to 0, there will be no additional print statements.
When debug_mode is set to 1, there will be print statements for the parsing of the input list for dugging purposes.
debug_mode is set to 0 by default.

Files:
Chromosome.py	-> Chromosome class to be imported in Puzzle 1, 2, and 3.
Chromosome1.py	-> Puzzle 1 implementation
ga.py 			-> main run file
ga_-_stats.py 	-> file to gather statistics on population size
ga_-_stats-2.py -> file to gather statistics on generations
GenAlg.py 		-> definition of function to run Genetic Algorithm
GenAlg2.py 		-> modified Genetic Algorithm used in ga.py
GenAlgEval.py 	-> modified Genetic Algorithm used in ga_-_stats-2.py
Illegal.py 		-> class used for fixing Puzzle 2 crossovers
ListParser.py 	-> class used for parsing an input file
Location.py 	-> class used for fixing Puzzle 2 crossovers
our_Puzzle1-1_sample.txt -> sample input for Puzzle 1
our_Puzzle1_sample.txt	 -> sample input for Puzzle 1
our_Puzzle2_sample.txt	 -> sample input for Puzzle 2
our_Puzzle3_sample.txt	 -> sample input for Puzzle 3
Piece.py 		-> class used to represent a piece of Puzzle 3
Puzzle2.py 		-> Puzzle 2 implementation
Puzzle3.py 		-> Puzzle 3 implementation
sample_puzzle1_list.txt	 -> provided example input for Puzzle 1
sample_puzzle2_list.txt	 -> provided example input for Puzzle 2
sample_puzzle3_list.txt	 -> provided example input for Puzzle 3
