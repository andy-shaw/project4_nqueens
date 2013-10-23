'''
Author: Andy Shaw
Date:   10/4/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03

This harness will run the hill climbing agent.  The harness will assure that the correct answer is
found using the boardScore module.  If the boardScore is 0, then the solution is correct.  The 
harness will restart the agent until a correct solution is found.
'''

import sys
import hillClimbingAgent as agent 
import printBoard as p
import boardScore as b
import array

def main(size, silent):
    
    
    #run the agent until correct solution is found
    while 1:
        answer = agent.hillClimbingAgent(size, silent)
        
        #newline between each restart
        if not silent: print ''
        
        #check to see if solution is correct
        if b.boardScore(answer) == 0:
            break
    
    #print solution
    # print agent.arrToString(answer)
    # p.printBoard(answer)
                
if __name__ == '__main__':
    #get board size as command line arg
    size = 0
    try:
        size = int(sys.argv[1])
    except:
        print 'invalid board size, try: $ python testHarnessHillClimbing.py #'
        print 'where # is an integer greater than or equal to 4'
        exit()
        
    #check to make sure board size is accurate
    if size < 4:
        print 'invalid board size: must be greather than or equal to 4'
        exit()
    
    #check to see if it should be run silent
    silent = False
    try:
        silent = sys.argv[2]
        if silent != 'SILENT':
            raise Exception()
    except:
        silent = False

    main(size, silent)