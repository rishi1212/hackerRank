#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    b,w = input().strip().split(' ')
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split(' ')
    x,y,z = [int(x),int(y),int(z)]
    if(x>y):
        if(x-y>z):
            x=y+z
        else:
            x=x
    else:
        x=x
    if(y>x):
        if(y-x>z):
            y=x+z
        else:
            y=y
    else:
        y=y
    print(b*x+w*y)