#!/bin/python

from Tools.scripts.treesync import raw_input

s, t = raw_input().strip().split(' ')
s, t = [int(s), int(t)]
a, b = raw_input().strip().split(' ')
a, b = [int(a), int(b)]
m, n = raw_input().strip().split(' ')
m, n = [int(m), int(n)]
apple = map(int, raw_input().strip().split(' '))
orange = map(int, raw_input().strip().split(' '))
appleDistance = []
orangeDistance = []
for i in apple:
    appleDistance.append(a + i)
for j in orange:
    orangeDistance.append(b + j)
count1 = 0
for i in appleDistance:
    if s <= i <= t:
        count1 += 1
print(count1)
count1 = 0
for i in orangeDistance:
    if s <= i <= t:
        count1 += 1
print(count1)
