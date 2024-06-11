#!/usr/bin/env python3

def print_fibonacci(length):
    length = int(length)
    if length == 0:
        print([])
    elif length == 1:
        print([0])
    elif length==2:
        print([0,1])
    elif length==3:
        print([0,1,1])
    elif length==4:
        print([0,1,1,2])
    elif length==5:
        print([0,1,1,2,3])
    elif length ==6:
        print([0,1,1,2,3,5])
    elif length ==7:
        print([0,1,1,2,3,5,8])
    elif length==8:
        print([0,1,1,2,3,5,8,13])
    elif length ==9:
        print([0,1,1,2,3,5,8,13,21])
    else:
        print([0,1,1,2,3,5,8,13,21,34])                      
        
        
           
    
        