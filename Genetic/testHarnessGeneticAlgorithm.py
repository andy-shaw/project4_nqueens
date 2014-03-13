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
import solution as s

'''
Main function.

The main retrieves the command line arguments.

'''
def main(boardSize, mutationRate, populationSize,silent):

    #run the agent until correct solution is found
    while 1:
        answer = agent.geneticAlgorithmAgent(boardSize, mutationRate, populationSize,silent)

        #newline between each restart
        if not silent: print '' 
        
        if s.solution(answer) == 0:
            break
            
    #print solution
    print agent.arrToString(answer)
    printBoard(answer)

'''
Author: Andy Shaw
Date:   10/4/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03

Using ASCII art, for an 8x8 board or less, display the positioning of the board
'''

def printBoard(state):
    #catch the condition of the board being too large
    if len(state) > 12:
        return None
    s = ''
    #top line
    s += '-'*(len(state)*2 + 1) + '\n'
    #body
    for row in range(len(state)):
        s += '|'
        for column in state:
            if column == row:
                s += 'X|'
            else:
                s += ' |'
        s += '\n'
    
    #bottom line
    s += '-'*(len(state)*2 + 1) + '\n'
    print s

'''
arg: boardSize int for an n x n board
arg: mutationRate float representing mutation rate
arg: populationSize int for the population to keep in memory
'''
if __name__ == '__main__':
    #get boardSize, mutationRate, populationSize
    boardSize = 0
    mutationRate = 0.0
    populationSize = 0
    try:
        boardSize = int(sys.argv[1])
        if boardSize < 4: raise Exception()
        
        mutationRate = float(sys.argv[2])
        if not 0 <= mutationRate<= 1: raise Exception()
        
        populationSize = int(sys.argv[3])
        if populationSize < 1: raise Exception()
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
        
    main(boardSize, mutationRate, populationSize,silent)