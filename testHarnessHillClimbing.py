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

def main():
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
    silent = None
    try:
        silent = sys.argv[2]
    except:
        pass
    
    #run the agent until correct solution is found
    while 1:
            if silent == 'SILENT': answer = agent.hillClimbingAgent(size, True)
            else: answer = agent.hillClimbingAgent(size); print ''
            
            #check to see if solution is correct
            if b.boardScore(answer) == 0:
                print agent.arrToString(answer)
                p.printBoard(answer)
                break
                
if __name__ == '__main__':
    main()