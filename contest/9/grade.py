#!/bin/python3

import sys

def lastDigit(a):
    rev=a%10
    return rev
n = int(input().strip())
for a0 in range(n):
    grade = int(input().strip())
    # your code goes here
    if(grade>=38):
        a=lastDigit(grade)
        if(a<5):
            if((5-a)<3):
                grade=grade+(5-a)
            else:
                pass
        elif(a==5 or a==0):
            pass
        else:
            if(a==8 or a==9):
                grade=grade+(10-a)
            else:
                pass
    else:
        pass
    print(grade)