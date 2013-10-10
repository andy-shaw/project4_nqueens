import array
import reproduce as r

x = array.array('i', [1,2,3,4,5,6])
y = array.array('i', [0,0,0,0,0,0])

print x
print y
print ''


for i in range(50): print r.reproduce(x,y)