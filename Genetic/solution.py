'''
Author: Andy Shaw
Date:   10/4/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03

This method will take in a state, and score it based on how many queens are 
attacking each other. return 0 on a solved board
param: state integer array holding state vector
return: integer score or rating
'''
def solution(state):
    attacks = 0
    
    #for each queen, see what it can attack
    #don't check columns, the way the state is represented means 2 cannot be in 
    #same column
    for queen in range(len(state)):
        #check any in same row
        for column in range(queen, len(state)):
            if state[queen] == state[column] and queen != column:
                attacks += 1

        #check diagonals
        #check after queen (from left to right)
        offset = 0
        pos = state[queen]
        for column in range(queen+1, len(state)):
            offset += 1
            if pos+offset == state[column] or pos-offset == state[column]:
                attacks += 1
    
    return attacks