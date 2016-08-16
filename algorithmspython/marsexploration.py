#!/bin/python3

import sys


S = input().strip()
a=int(len(S)/3)
expected=[]
for i in range(0,a):
    expected.append("SOS")
ans1="".join(expected)
count=0
for i in range(0,len(S)):
    if(S[i]!=ans1[i]):
        count+=1
print(count)