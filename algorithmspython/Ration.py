#!/bin/python3

import sys


N = int(input().strip())
B = [int(B_temp) for B_temp in input().strip().split(' ')]
sum1=sum(B)
count=0
if(sum1%2==1):
    print("NO")
else:
    for i in range(0,N):
        if(B[i]%2!=0):
            B[i]=B[i+1]
            B[i+1]=B[i+1]+1
            count+=2
    print(count)
