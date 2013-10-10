import array
import mutate as m


x = array.array('i', [0,0,0,0,0,0,0,0])

#test mutation rate of 0
print 'testing mutation rate of 0'
for i in range(500):
    y = m.mutate(x, 0)
    if y != x:
        print 'mutation failed test'
        exit()
print 'passed rate of 0'

#test mutation rate of 1
print 'testing mutation rate of 1'
for i in range(500):
    y = m.mutate(x, 1)
    if y == x:
        print 'mutation failed test'
        exit()
print 'passed rate of 1'

#output for examples of it working
mutations = 0
for i in range(5000): 
    y = m.mutate(x, .008)
    if y != x: mutations += 1

print 'mutation rate of .008 at 5000 tests has {0} mutations'.format(mutations)