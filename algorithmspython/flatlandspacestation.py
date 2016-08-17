#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
if(n==m):
    print(0)
else:
    station = 0

    for i in range (n):
        temp = 100000000000
        for j in range (m):
            if(abs(i-c[j]) < temp):
                temp = abs(i-c[j])
        if(temp > station):
            station = temp
    print(station)



