'''
Author: Andy Shaw
Date:   10/4/2013
Course: CSE 3521 - Survey of Artificial Intelligence
                   Assignment03

Using ASCII art, for an 30x30 board or less, display the positioning of the board
'''

def printBoard(state):
    #catch the condition of the board being too large
    if len(state) > 30:
        return None
    s = ''
    #top line
    s += '-'*(len(state)*2 + 1) + '\n'
    #body
    for row in range(len(state)):
        s += '|'
        for column in state:
            if column == row:
                s += 'X|'
            else:
                s += ' |'
        s += '\n'
    
    #bottom line
    s += '-'*(len(state)*2 + 1) + '\n'
    print s