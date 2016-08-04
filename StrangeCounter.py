#!/bin/python3

import sys


t = int(input().strip())
n = 2;
while (3 * (n - 1) < t):
    n = 2 * n;
print((3 * (n - 1) - t + 1))


