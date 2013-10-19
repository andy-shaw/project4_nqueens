'''
Author: Andy Shaw
Date:   10/19/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03                   

This harness will run the genetic agent.  The harness will assure that the correct answer is
found using the solution module.  If the solution is 0, then the solution is correct.  The 
harness will restart the agent until a correct solution is found.
'''

import sys
import geneticAlgorithmAgent as agent
import printBoard as p
import solution as s

'''
Main function.

The main retrieves the command line arguments.
arg: boardSize int for an n x n board
arg: mutationRate float representing mutation rate
arg: populationSize int for the population to keep in memory
'''
def main():
    #get boardSize, mutationRate, populationSize
    boardSize = 0
    mutationRate = 0.0
    populationSize = 0
    try:
        boardSize = int(sys.argv[1])
        mutationRate = float(sys.argv[2])
        populationSize = int(sys.argv[3])
    except:
        print 'invalid arguments: boardSize mutationRate populationSize'
        print 'boardSize: int < 3; mutationRate: float [0,1]; populationSize: int > 0'
        exit()
        
    #check to see if it should be run silent
    silent = False
    try:
        silent = sys.argv[4]
        if silent != 'SILENT':
            raise Exception()
    except:
        silent = False
        
    #run the agent until correct solution is found
    while 1:
        answer = agent.geneticAlgorithmAgent(boardSize, mutationRate, populationSize,silent)

        #newline between each restart
        if not silent: print '' 
        
        if s.solution(answer) == 0:
            break
            
    #print solution
    print agent.arrToString(answer)
    p.printBoard(answer)
    
if __name__ == '__main__':
    main()