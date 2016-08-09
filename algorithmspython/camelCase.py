import sys


s = input().strip()
count=1
for i in range(0,len(s)):
    if(ord(s[i])>=65 and ord(s[i])<=90):
        count+=1
print(count)