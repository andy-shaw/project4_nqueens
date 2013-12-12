'''
clean out all .pyc files
'''
def main():
    '''clean out all .pyc files'''
    import os
    files = os.listdir('.')
    for file in files:
        if file[-4:] == '.pyc':
            os.system('del ' + file)
            print 'removed', file
            
    print 'clean complete'
    
if __name__ == '__main__':
    main()