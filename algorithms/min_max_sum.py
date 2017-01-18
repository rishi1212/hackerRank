#!/bin/python

a=list(map(int,input().split(" ")))
a.sort()
sum1=0
sum2=0
for i in range(0,len(a)-1):
    sum1+=a[i]
for j in range(1,len(a)):
    sum2+=a[j]
print (sum1,sum2)