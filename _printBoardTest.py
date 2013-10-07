import printBoard as p
import array
import random
import sys



x = array.array('i')

for i in range(int(sys.argv[1])): x.append(random.randint(0,int(sys.argv[1]) - 1))

p.printBoard(x)
