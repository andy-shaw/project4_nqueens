'''
Author: Andy Shaw
Date:   10/10/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03

This method will take in a state, and score it based on how many queens are not
attacking each other.
param: state integer array holding state vector
return: integer score or rating
'''
def boardScore(state):
    noAttacks = 0
    
    #for each queen, see what it can attack
    #don't check columns, the way the state is represented means 2 cannot be in 
        #same column
    for queen in range(len(state)):
        #check against other queens
        for otherQueen in range(queen, len(state)):
            #if other queen is not in same row as this queen
            if state[queen] != state[otherQueen]:
                #check diagonals
                offset = otherQueen - queen
                if (state[otherQueen] + offset != state[queen] and 
                    state[otherQueen] - offset != state[queen]):
                    noAttacks += 1
                

    return noAttacks