'''
Author: Andy Shaw
Date:   10/4/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03

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