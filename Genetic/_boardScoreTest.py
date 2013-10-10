import boardScore as b
import array
a1 = array.array('i', [2,4,7,4,8,5,5,2])
a2 = array.array('i', [3,2,7,5,2,4,1,1])
a3 = array.array('i', [2,4,4,1,5,1,2,4])
a4 = array.array('i', [3,2,5,4,3,2,1,3])

assert(b.boardScore(a1) == 24)
assert(b.boardScore(a2) == 23)
assert(b.boardScore(a3) == 20)
assert(b.boardScore(a4) == 11)

