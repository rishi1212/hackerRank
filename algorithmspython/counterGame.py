import math
from math import log2
from math import floor
def genlist(x):
    if x==1:
        return False
    elif (log2(x))%1==0:
        return not genlist(int(x/2))
    else:
        return not genlist(x-2**floor(log2(x)))

tcs=int(input())
for tc in range(tcs):
    sa=int(input())
    if genlist(sa):
        print("Louise")
    else:
        print("Richard")