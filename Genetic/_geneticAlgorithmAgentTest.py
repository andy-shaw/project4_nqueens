import geneticAlgorithmAgent as agent
import solution as s

x = None
while 1:
    x = agent.geneticAlgorithmAgent(5, .008, 20)
    if s.solution(x) == 0:
        break
print x