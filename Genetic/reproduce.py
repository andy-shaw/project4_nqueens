'''
Author: Andy Shaw
Date:   10/10/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03
                   
This program will take two input states and create a population.

Note: a constraint is that len(state1) = len(state2)
param: state1 int array representing the first parent state
param: state2 int array representing the second parent state
return: new array produced from parts of state1 and state2
'''
def reproduce(state1, state2):
    import random
    import array
    
    #choose cut point to split
    divider = random.randint(1, len(state1)-1)
    
    #possible 2 children can form: 
        #subset from state1|subset from state2
        #subset from state2|subset from state1
    child1 = state1[:divider]
    child1.extend(state2[divider:])
    child2 = state2[:divider]
    child2.extend(state1[divider:])
    
    #randomly choose a child to survive
    if random.randint(0,1) == 0:
        return child1
    else:
        return child2