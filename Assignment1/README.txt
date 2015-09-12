To run:

$python astar.py <Map File> <Heuristic (1-6)>

For example, to run world1 with heuristic 2:
$python astar.py Our_Worlds\world1_1.txt 2

In the file astar.py, there is a variable "debug_mode" on line 46.
When debug_mode is set to 0, there will be no additional print statements besides the analysis of the search.
When debug_mode is set to 1, there will be print statements throughtout the A* search for debugging purposes.
debug_mode is set to 0 by default.

Worlds are located in the directory ./Our_Worlds.
An explanation to what each world represents can be found in our write-up.