def main():
    import testHarnessHillClimbing as test
    import time

    times = list()

    tries = 10
    size = 15

    for x in range(tries):
        if x%(tries/5) == 0: print 'iteration:', x
        start = time.time()
        y = test.main(size, True)
        finish = time.time()
        times.append(finish-start)

        
    print "\navg:    {0}\nbest:   {1}\nworst:  {2}\nmedian: {3}".format(sum(times)/float(tries), min(times), max(times), med(times))

def med(times):
    return sorted(times)[len(times)/2]
    
if __name__ == '__main__': main()