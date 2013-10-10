'''
clean out all .pyc files
'''

import os
files = os.listdir('.')
for file in files:
    if file[-4:] == '.pyc':
        os.system('del ' + file)
        
print 'clean complete'