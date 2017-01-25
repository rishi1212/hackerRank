import sys


h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()
lengthOfWord=len(word)
area=[]
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in word:
    a=0
    for j in alpha:
        if (i==j):
            area.append(h[a])
        a+=1
print(lengthOfWord*max(area))