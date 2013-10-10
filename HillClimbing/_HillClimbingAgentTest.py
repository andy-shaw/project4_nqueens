
import hillClimbingAgent as agent, array
import printBoard as p
import boardScore as b
import sys
import time

arr1 = array.array('i', [4,5,6,3,4,5,6,5])
times = list()
try:
    for x in range(5):
        start = time.time()
        while 1:
            answer = agent.hillClimbingAgent(int(sys.argv[1]),True)
            #print ''
            if b.boardScore(answer) == 0:
                #print agent.arrToString(answer)
                #p.printBoard(answer)
                break
        finish = time.time()
        times.append(finish-start)
except:
    pass
finally:
    print "total:", len(times)
    print "avg: %.4f seconds"%(sum(times)/len(times))
    print "min: %.4f seconds"%(min(times))
    print "max: %.4f seconds"%(max(times))
