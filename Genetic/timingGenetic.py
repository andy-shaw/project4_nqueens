import testHarnessGeneticAlgorithm as agent
import time
import winsound



# for size in range(4, 9):

    # print 'timing population varients, size:', size
    
    # file = open('./analysis/' + str(size) + '.txt', 'w')
    
    # for pop in range(5, 50, 5):
        # for x in range(5):
            # start = time.time()
            # agent.main(size, .008, pop, True)
            # finish = time.time()
            # file.write(str(finish-start) + '\n')
        
    # file.write('\n---------------------------------------\n')
    
    # print 'timing mutation varients, size:', size
    # mut = 0.0
    # while mut <= 0.9:
        # for x in range(5):
            # start = time.time()
            # agent.main(size, mut, 10, True)
            # finish = time.time()
            # file.write(str(finish-start) + '\n')
        # mut += 0.1
        
    # file.close()
    
for size in range(4,9):

    print 'timing size:', size

    file = open('./analysis/base_' + str(size) + '.txt', 'w')
    
    for x in range(30):
        start = time.time()
        agent.main(size, .008, 100, True)
        finish = time.time()
        file.write(str(finish-start) + ',')
        
    file.close()
    
print 'timing complete'
winsound.Beep(500, 1000)