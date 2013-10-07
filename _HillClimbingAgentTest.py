
import hillClimbingAgent as agent, array
import boardScore as b
import winsound as w
import time

arr1 = array.array('i', [4,5,6,3,4,5,6,5])
times = list()
for x in range(100):
    start = time.time()
    while 1:
        answer = agent.hillClimbingAgent(5, True)
        if b.boardScore(answer) == 0:
            break
    #print agent.arrToString(answer)
    finish = time.time()
    times.append(finish-start)
print "total:", len(times)
print "avg: %.4f seconds"%(sum(times)/len(times))
print "min: %.4f seconds"%(min(times))
print "max: %.4f seconds"%(max(times))
