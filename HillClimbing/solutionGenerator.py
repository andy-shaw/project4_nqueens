solutions = open('solutions.txt', 'w')

import harness
import array

for i in range(4,30):
    solutions.write(harness.arrToString(harness.hillClimbingAgent(i, True)) + '\n')
    print 'completed:', i

solutions.close()
print 'Script complete'