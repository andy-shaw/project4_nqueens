import geneticAlgorithmAgent as agent
import solution as s
import sys

x = None
silent = False
try:
    if sys.argv[1]: silent = True
except:
    pass
while 1:
    x = agent.geneticAlgorithmAgent(5, .008, 5, silent)
    if s.solution(x) == 0:
        break
print x