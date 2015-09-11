#!/usr/bin/env python

def AStar(world, start, goal): #start and goal are cells
    print "Running A*"

    visited = [] #nodes
    frontier = [] #nodes
    pathList = [] #nodes

    frontier.append(start)

    while frontier is not empty 
        current = findLowestCost(frontier)
        if(current is goal)
            return reconstructPath() #this will be a thing

        frontier.remove(current)
        visited.append(current)

        for each neighbor in current.neighbors
            if (neighbor is in visited) or (not neighbor.isValid())
                continue

            localDir = findDirection(currentCell, moveCell)
            if shouldBashHa(current, neighbor)
                neighbor = neighbor.neighbors[FindDirecton(localDir)]
                neighbor.actionList = 
            # action cost needs to be a function that calculates the cost of moving from 
            # a cell to the specified neighbor cell based on the orientation and movement costs
            tentativeEstCost = current.costSoFar + actionCost() + neighbor.heuristic

            if (neighbor not in frontier) or (tentativeEstCost < estCost)
                neighbor.parent = current #replace this by appending the action list
                neighbor.costSoFar = current.costSoFar + actionCost(current, neighbor)
                neighbor.estCost = tentativeEstCost
                if neighbor not in frontier
                    frontier.append(neighbor)
    print "A* failed"

def shouldBashHa(current, neighbor):
    localDir = findDirection(currentCell, moveCell)
    if canBash() and (neighbor.getCurrentCell().getComplexity() > 3)
        tentCostBash = actionCost(current.getCurrentCell(), neighbor.getCurrentCell(), True) + neighbor.neighbors[localDir].heuristic
        tentCostDrive = actionCost(current.getCurrentCell(), neighbor.getCurrentCell(), False) + neighbor.heuristic
        if tentCostBash < tentCostDrive
            return True
    else
        return False





def actionCost(currentCell, moveCell, isBash):
    localDir = findDirection(currentCell, moveCell)
    turningCost = turningCalc(localDir)

    if isBash
        return turningCost + moveCell.neighbors[localDir].getComplexity() + 3
    else
        return turningCost + moveCell.getComplexity()



                
