'''
Author: Andy Shaw
Date:   10/4/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03

This agent is based off the Hill Climbing algorithm found on slide 5 of the Week04b-Optimization 
slides.

Note: Next choice is purely based on the heap's return algorithm.  In the case of a tie, it is not
going to be random.

param: boardsize integer board size
returns: state that is a solution
'''

import heapq
import array

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
        
        #print status
        if not silent: print 'Iteration:{0}\tState:<{1}>\tBest Child Score:{2}'.format(
                        i, arrToString(currNode[1]), nextNode[0])
        
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
    for queen in range(len(state)):
        #check any in same row
        # for column in range(queen, len(state)):
            # if state[queen] == state[column] and queen != column:
                # attacks += 1

        #check diagonals
        #check after queen (from left to right)
        offset = 0
        pos = state[queen]
        for column in range(queen+1, len(state)):
            offset += 1
            if pos+offset == state[column] or pos-offset == state[column]:
                attacks += 1
            if state[queen] == state[column] and queen != column:
                attacks += 1
            
    return attacks