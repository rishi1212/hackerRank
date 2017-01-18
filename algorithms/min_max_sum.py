a=list(map(int,input().split(" ")))
a.sort()
sum1=0
sum2=0
for i in range(1,a.length):
    sum1+=i
for j in range(0,a.length-1):
    sum2+=j
print (sum1,sum2)