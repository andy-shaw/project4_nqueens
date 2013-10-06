import successor as s, boardScore as b, array

bookexample = array.array('i', [18,14,14,15,17,18,14
                               ,12,16,12,14,14,14,14
                               ,14,13,18,14,17,16,13
                               ,13,15,13,15,18,15,17
                               ,13,12,15,13,15,15,12
                               ,12,14,12,16,14,14,14
                               ,14,12,14,13,16,15,12
                               ,14,16,14,16,16,16,18])

arr1 = array.array('i', [4,5,6,3,4,5,6,5])
children = s.successor(arr1)
board = array.array('i')
for child in children:
    board.append(b.boardScore(child))
    
check = True
for i in range(len(board)):
    if bookexample[i] != board[i]:
        check = False
        
if check: print 'passed book example'