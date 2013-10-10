'''
Author: Andy Shaw
Date:   10/10/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03
                   
This method will perform a mutation on the the input string based on a provided mutation rate.

param: state int array representing the state to be mutated
param: mutationRate double for mutation percentage
return: new state with mutation applied
'''

def mutate(state, mutationRate):
    import random
    
    newState = copyArr(state)
    #check for mutation on each index
    for pos in range(len(state)):
        #check to see if mutation occurs
        if random.random() <= mutationRate:
            newState[pos] = random.randint(0, len(state)-1)
        
    return newState
        
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