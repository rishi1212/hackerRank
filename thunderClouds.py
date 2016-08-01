#!/bin/python3

import sys


n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
ans = 0
i = 0
while i < n - 1:
    if i + 2 >= n or c[i + 2] == 1:   # Not possible to make a jump of size 2
        i = i + 1
        ans = ans + 1
    else:
        i = i + 2
        ans = ans + 1
print (ans)
