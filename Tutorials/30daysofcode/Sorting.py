#!/bin/python3

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
numOfSwaps=0
for i in range(0,n):
    for j in range(0,n-1):
        if (a[j] > a[j + 1]):
            a[j], a[j + 1]=a[j+1],a[j]
            numOfSwaps+=1

    if (numOfSwaps == 0):
        break;

print("Array is sorted in "+str(numOfSwaps)+" swaps.")
print("First Element: "+str(a[0]))
print("Last Element: "+str(a[n-1]))