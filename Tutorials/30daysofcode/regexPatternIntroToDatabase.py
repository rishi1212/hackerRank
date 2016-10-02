#!/bin/python3

import sys


N = int(input().strip())
names=[]
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if(emailID[-10:]=='@gmail.com'):
        names.append(firstName)
names.sort()
for i in names:
    print(i)