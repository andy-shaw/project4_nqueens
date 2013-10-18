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
from solution import solution
from boardScore import boardScore
import reproduce as r
import mutate as m
import heapq

def geneticAlgorithmAgent(boardSize, mutationRate, populationSize, silent=False):
    #generate the population of state nodes
    import random
    generation = list()
    for i in range(populationSize):
        newState = array.array('i')
        for x in range(boardSize):
            newState.append(random.randint(0, boardSize-1))
        generation.append(newState)
    
    iteration = 0
    totalFitness = 0
    newTotalFitness = 0
    
    #enter genetic algorithm until less than 5% fitness improvement is seen
    while 1:

        newTotalFitness = totalFitness
        #score generation
        scoredGeneration, totalFitness = score(generation, populationSize)
        
        #if score is not a 5% improvement then return current gen
        if float(newTotalFitness)/totalFitness > .95:
            return sorted(scoredGeneration, reverse=True)[1][-1]
    
        #output iteration, most fit individual and their score
        if not silent: print 'Iteration: {0}\tMost Fit Individual: {1}\tScore: {2}'.format(
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
            x = r.reproduce(generation[i], generation[i+1])
            # print 'parent1:\t', generation[i], 'parent2:\t', generation[i+1]
            # print 'child:\t\t',x
            children.append(x)
        
        #mutate the children
        for child in children:
            child = m.mutate(child, mutationRate)
            
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