# pass terminal arguments

    Pass terminal/command line arguments to python program
    
# code

    import sys
    
    print('The first arguement length is {}, the argument listis {}'.format(len(sys.argv),sys.argv))

    for i,item in enumerate(sys.argv):
        
        if i==0:
            print('the filename is'.format(item))
        else:
            print('arguement {} is: "{}"'.format(i,item))
