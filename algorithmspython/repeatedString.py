#!/bin/python3

import sys


s = input().strip()
n = int(input().strip())
count = 0
for i in s:
    if i=='a':
        count+=1

l = len(s)
m = n//l
t = n%l
h =0
for i in range(t):
    if s[i]=='a':
        h+=1

ans = m *count+h
print(ans)