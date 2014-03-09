'''
Author: Andy Shaw
Date:   10/10/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03
                   
This agent is based off the Genetic Algorithm found in the Week04b-Optimization slides.  The
algorithm will terminate when it sees less than a 5% improvement

param: boardSize int telling board size
param: mutationRate double for mutation rate percentage
param: populationSize population size for each iteration
return: state that is a solution
'''

import array
import heapq
from solution import solution

def geneticAlgorithmAgent(boardSize, mutationRate, populationSize, silent=False):
    #generate the population of state nodes
    import random
    generation = list()
    for i in range(populationSize):
        newState = array.array('i')
        for x in range(boardSize):
            newState.append(random.randint(0, boardSize-1))
        generation.append(newState)
    
    iteration = 1
    totalFitness = 0
    newTotalFitness = 0
    n = 0
    
    #max fitness is n(n-1)/2 (comment is diff from code for efficiency)
    maxFitness = (boardSize*(boardSize-1))
    #termination percentage is 1 - 1/(maxFitness) * 2
    terminationPercentage = 1.0 - 1.0/maxFitness
    
    #enter genetic algorithm until less than 5% fitness improvement is seen
    while 1:

        newTotalFitness = totalFitness
        #score generation
        scoredGeneration, totalFitness = score(generation, populationSize)
        
        #if total fitness is 0, set it to 1 so there is no division by 0
        if totalFitness == 0:
            totalFitness = 1
        
        #if score is not better than the termination percentage, try for 5 times
        if float(newTotalFitness)/totalFitness > terminationPercentage:
            n += 1
            if n >= 5: return sorted(scoredGeneration, reverse=True)[1][-1]
        # else:
            # n = 0
    
        #output iteration, most fit individual and their score
        if not silent: 
            print 'Iteration: {0}\tMost Fit Individual: {1}\tScore: {2}'.format(
                        iteration, arrToString(scoredGeneration[-1][1]), scoredGeneration[-1][0])
            
        #apply percentages of selection to fitness of each state
        temp = list()
        for state in scoredGeneration:
            temp.append((float(state[0])/totalFitness, state[1]))
        scoredGeneration = temp
        
        #sum up the percentages in each state
        #set each percentage in such a way, that the most fit (in position 0) is at 1.0
        for i in range(len(scoredGeneration) - 2, -1, -1):
            scoredGeneration[i] = (scoredGeneration[i+1][0] + scoredGeneration[i][0], scoredGeneration[i][1])
            
        #choose double the generation as the state to child ratio is 2:1
        generation = list()
        for i in range(2*populationSize):
            selection = random.random()
            #when the random number is less than the current percentage, it is in that range
            for state in range(len(scoredGeneration)):
                if selection >= scoredGeneration[state][0]:
                    generation.append(scoredGeneration[state][1])
                    break
                    
        #create the children
        children = list()
        for i in range(0, len(generation) - 1, 2):
            x = reproduce(generation[i], generation[i+1])
            children.append(x)
        
        #mutate the children
        for child in children:
            child = mutate(child, mutationRate)
            
        #check to see if a solution was found
        for child in children:
            if solution(child) == 0:
                return child
                
        #combine children with the parents for a total generation
        generation = list()
        for child in children: generation.append(child)
        for parent in scoredGeneration: generation.append(parent[1])
        
        iteration += 1
'''
Score each state, and apply its selection percentage to the first item in the tuple.

param: generation list of int arrays 
param: populationSize int of max size of population
return: scoredGeneration generation that has the score as the fitness percentage as the first
item in the tuple, totalFitness int of summed fitness
'''
def score(generation, populationSize):
    #score each state
    scoredGeneration = list()
    for state in generation:
        scoredGeneration.append((boardScore(state), state))
    scoredGeneration = sorted(scoredGeneration, reverse=True)

    
    #trim to population size of top fitness scorers
    temp = list()
    for i in range(populationSize):
        temp.append(scoredGeneration[i])
    scoredGeneration = temp
        
    #sum fitness scores
    totalFitness = 0
    for state in scoredGeneration:
        totalFitness += state[0]
    
    return scoredGeneration, totalFitness
    
'''
Create string that represents contents of array separated by commas
param: arr array to be converted
return: string representation of array
'''
def arrToString(arr):
    x = arr.tolist()
    s = ''
    for item in x:
        s += str(item) + ','
    return s[:-1]

'''
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

'''
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