#!/bin/python3

import sys


n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
distance=[]
for i in range(0,len(A)):
    for j in range(0,len(A)):
        if(j==i):
            continue
        if(A[i]==A[j]):
            distance.append(abs(i-j))
if(len(distance)>0):
    print(min(distance))
else:
    print(-1)