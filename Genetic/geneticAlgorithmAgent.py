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

def geneticAlgorithmAgent(boardSize, mutationRate, populationSize):
    #generate the population of state nodes
    import random
    generation = list()
    for i in range(populationSize):
        newState = array.array('i')
        for x in range(boardSize):
            newState.append(random.randint(0, boardSize-1))
        generation.append(newState)
    
    iteration = 0
    
    #enter genetic algorithm until less than 5% fitness improvement is seen
    while 1:
        #score each state
        scoredGeneration = list()
        for state in generation:
            scoredGeneration.append((boardScore(state), state))
        scoredGeneration = sorted(scoredGeneration)
        
        #output iteration, most fit individual and their score
        print 'Iteration: {0}\tMost Fit Individual: {1}\tScore: {2}'.format(
                iteration, arrToString(scoredGeneration[-1][1]), scoredGeneration[-1][0])
            
        #sum fitness scores
        totalFitness = 0
        for state in scoredGeneration:
            totalFitness += state[0]
            
        #calculate highest fitness for termination case
        maxFitness = -1
        for state in scoredGeneration:
            maxFitness = max(maxFitness, state[0])
            
        #apply percentages of selection to fitness of each state
        temp = list()
        for state in scoredGeneration:
            temp.append((float(state[0])/totalFitness, state[1]))
        scoredGeneration = temp
        
        #sum up the percentages in each state
        for i in range(len(scoredGeneration) - 2, -1, -1):
            scoredGeneration[i] = (scoredGeneration[i+1][0] + scoredGeneration[i][0], scoredGeneration[i][1])
        
        #choose double the generation as the state to child ratio is 2:1
        generation = list()
        for i in range(2*populationSize):
            selection = random.random()
            #when the random number is less than the current percentage, it is in that range
            for state in range(len(scoredGeneration)):
                if selection < scoredGeneration[state][0]:
                    generation.append(scoredGeneration[state][1])
                    break
                    
        #create the children
        children = list()
        for i in range(0, len(generation) - 1, 2):
            children.append(r.reproduce(generation[i], generation[i+1]))
        
        #mutate the children
        for child in children:
            child = m.mutate(child, mutationRate)
            
        #check to see if a solution was found
        for child in children:
            if solution(child) == 0:
                return child
            
        #find max child fitness
        childFitnesses = array.array('i')
        for child in children:
            childFitnesses.append(boardScore(child))
        maxChildFitness = -1
        for fitness in childFitnesses:
            maxChildFitness = max(maxChildFitness, fitness)
            
        #if there has been less than 5% fitness improvement, terminate program
        print float(maxChildFitness)/maxFitness
        if float(maxChildFitness)/maxFitness > .95:
            return sorted(children)[-1]
        
        iteration += 1
        
        
def arrToString(arr):
    x = arr.tolist()
    s = ''
    for item in x:
        s += str(item) + ','
    return s[:-1]