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
import array

def main(size, silent):
    
    #run the agent until correct solution is found
    while 1:
        answer = hillClimbingAgent(size, silent)
        
        #newline between each restart
        if not silent: print ''
        
        #check to see if solution is correct
        if boardScore(answer) == 0:
            break
    
    #print solution
    print arrToString(answer)
    printBoard(answer)


'''
This agent is based off the Hill Climbing algorithm found on slide 5 of the Week04b-Optimization 
slides.

Note: Next choice is purely based on the heap's return algorithm.  In the case of a tie, it is not
going to be random.

param: boardsize integer board size
returns: state that is a solution
'''

import heapq
import os
import time

def hillClimbingAgent(boardSize, silent=False):
    #create initial state at random
    import random
    initial = array.array('i')
    for i in range(boardSize):
        initial.append(random.randint(0, boardSize-1))

    currNode = (boardScore(initial), copyArr(initial))
    i = 1
    while 1:
        childrenHeap = list()
        
        #find successors
        children = successor(currNode[1])
        
        #rate each resulting board and add to heap
        for child in children:
            heapq.heappush(childrenHeap, (boardScore(child), child))
        
        #pull out next best choice
        nextNode = heapq.heappop(childrenHeap)
        
        #print status for each iteration
        if not silent: print 'Iteration:{0}\tState:<{1}>\tBest Child Score:{2}'.format(
                        i, arrToString(currNode[1]), nextNode[0])
        
        #print board at each iteration
        # if not silent and time.clock() < 15: 
        #     os.system('cls')
        #     print i-1
        #     printBoard(currNode[1])
        #     time.sleep(.08)
        # else:
        #     os.system('cls')
        #     print 'Finding a solution, please wait'

        #check if solution
        if nextNode[0] == 0:
            return nextNode[1]
            
        #if currNode is less than, then it is the best solution on the board, heap will assure that
        if currNode[0] <= nextNode[0]:
            return currNode[1]
            
        #try again on the nextNode
        currNode = nextNode
        i+=1
        
def arrToString(arr):
    x = arr.tolist()
    s = ''
    for item in x:
        s += str(item) + ','
    #drop last comma and return
    return s[:-1]
        
'''
The successor function will return a set of all the possible child states of
the input state

param: state array of row positions
return: set of possible child states
'''
def successor(state):
    import array
    children = list()
    
    #for each column, the children will be the queen in every other row
    #len(state) is one dimension of the board
    for queen in range(len(state)):
        for newPos in range(len(state)):
            newState = copyArr(state)
            
            #skip if pos is the queen's current position
            if newPos != state[queen]:
                newState[queen] = newPos
                children.append(newState)
    
    return children
'''
Copy array into a new array.
Note: Python arr2 = arr1 will make equivalent by reference, this makes a new array

param: arr1 array to be copied
return: new identical array
'''
def copyArr(arr1):
    import array
    newArr = array.array(arr1.typecode)
    for item in arr1:
        newArr.append(item)
    return newArr

'''
This method will take in a state, and score it based on how many queens are 
attacking each other.
param: state integer array holding state vector
return: integer score or rating
'''
def boardScore(state):
    attacks = 0
    
    #for each queen, see what it can attack
    #don't check columns, the way the state is represented means 2 cannot be in 
    #same column
    for queenColumn in range(len(state)):
        #check right of queenColumn (from left to right)
        offset = 0
        pos = state[queenColumn]
        for seekColumn in range(queenColumn+1, len(state)):
            offset += 1
            #check diagonal
            if pos+offset == state[seekColumn] or pos-offset == state[seekColumn]:
                attacks += 1
            #check row
            if state[queenColumn] == state[seekColumn] and queenColumn != seekColumn:
                attacks += 1
            
    return attacks

'''
Using ASCII art, for a board, display the positioning of pieces on the board
'''
def printBoard(state):
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