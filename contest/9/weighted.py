#!/bin/python3

s = input().strip()
n = int(input().strip())
alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
weight=[]
for i in range(1,27):
    weight.append(i)
a=[]
for i in s:
    if(i not in a):
        a.append(i)
w=[]
for i in a:
    w.append(alphabets.index(i)+1)
for i in a:
    count=0
    count=s.count(i)
    if(count>1):
        if(count==2):
            w.append(count*(alphabets.index(i)+1))
        else:
            copy=count
            while(copy>=2):
                w.append(copy*(alphabets.index(i)+1))
                copy-=1
for a0 in range(n):
    x = int(input().strip())
    if(x in w):
        print("Yes")
    else:
        print("No")