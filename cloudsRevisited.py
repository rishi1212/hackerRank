import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(c_temp) for c_temp in input().strip().split(' ')]
e=100
for i in range(0,n,k):
    if(c[i]==1):
        e-=3
    if(c[i]==0):
        e-=1
print (e)