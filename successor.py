'''
Author: Andy Shaw
Date:	10/4/2013
Course: CSE 3521 - Survey of Artificial Intelligence
				   Assignment03
'''

'''
The successor function will return a set of all the possible child states of
the input state

param: state array of column positions
return: set of possible child states
'''
def successor(state):
	import array
	children = {}
	
	#for each row, each child will be the queen in any other position