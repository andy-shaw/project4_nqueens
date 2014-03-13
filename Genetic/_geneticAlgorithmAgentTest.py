import geneticAlgorithmAgent as agent
from printBoard import printBoard
import solution as s
import sys
import time

x = None
silent = False
try:
    if sys.argv[1]: silent = True
except:
    pass
    
size = 6
mut = .008
gen = 100
    
print '\n\nTesting for n={0}, mutRate={1}, gen={2}\n\n'.format(size,mut,gen)
start = time.time()
while 1:
    x = agent.geneticAlgorithmAgent(size, mut, gen ,silent)
    if s.solution(x) == 0:
        break
finish = time.time()
print agent.arrToString(x)
printBoard(x)
print 'took:', finish-start