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
import solution as s
import boardScore as b
import reproduce as r
import mutate as m
import heapq

def geneticAlgorithmAgent(boardSize, mutationRate, populationSize):
    #generate the population of parent nodes
    import random
    parents = list()
    for i in range(populationSize):
        newParent = array.array('i')
        for x in range(boardSize):
            newParent.append(random.randint(0, boardSize-1))
        parents.append(newParent)
    
    iteration = 0
    
    #enter genetic algorithm until less than 5% fitness improvement is seen
    while 1:
        #score each parent
        scoredParents = list()
        for parent in parents:
            scoredParents.append((b.boardScore(parent), parent))
        scoredParents = sorted(scoredParents)
        
        #output iteration, most fit individual and their score
        print 'Iteration: {0}\tMost Fit Individual: {1}\tScore: {2}'.format(
                iteration, arrToString(scoredParents[-1][1]), scoredParents[-1][0])
            
        #sum fitness scores
        totalFitness = 0
        for parent in scoredParents:
            totalFitness += parent[0]
            
        #calculate highest fitness for termination case
        maxFitness = -1
        for parent in scoredParents:
            maxFitness = max(maxFitness, parent[0])
            
        #apply percentages of selection to fitness of each parent
        temp = list()
        for parent in scoredParents:
            temp.append((float(parent[0])/totalFitness, parent[1]))
        scoredParents = temp
        
        #sum up the percentages in each parent
        for i in range(len(scoredParents) - 2, -1, -1):
            scoredParents[i] = (scoredParents[i+1][0] + scoredParents[i][0], scoredParents[i][1])
        
        #choose double the parents as the parent to child ratio is 2:1
        parents = list()
        for i in range(2*populationSize):
            selection = random.random()
            #when the random number is less than the current percentage, it is in that range
            for parent in range(len(scoredParents)):
                if selection < scoredParents[parent][0]:
                    parents.append(scoredParents[parent][1])
                    break
                    
        #create the children
        children = list()
        for i in range(0, len(parents) - 1, 2):
            children.append(r.reproduce(parents[i], parents[i+1]))
        
        #mutate the children
        for child in children:
            child = m.mutate(child, mutationRate)
            
        #check to see if a solution was found
        for child in children:
            if s.solution(child) == 0:
                return child
            
        #find max child fitness
        childFitnesses = array.array('i')
        for child in children:
            childFitnesses.append(b.boardScore(child))
        maxChildFitness = -1
        for fitness in childFitnesses:
            maxChildFitness = max(maxChildFitness, fitness)
            
        #if there has been less than 5% fitness improvement, terminate program
        print float(maxChildFitness)/maxFitness
        if float(maxChildFitness)/maxFitness > .95:
            return sorted(children)[-1]
        
        parents = children
        iteration += 1
        
        
def arrToString(arr):
    x = arr.tolist()
    s = ''
    for item in x:
        s += str(item) + ','
    return s[:-1]