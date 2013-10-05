'''
Author: Andy Shaw
Date:   10/4/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03

This method will take in a state, and score it based on how many queens are attacking each other.
param: state integer array holding state vector
return: integer score or rating
'''
def boardScore(state):
    #for each queen, see what it can attack