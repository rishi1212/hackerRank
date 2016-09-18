n=int(input())
a1=list(map(int,input().split(" ")))
a2=list(map(int,input().split(" ")))
array1=[]
for i in range(0,n):
    for j in range(0,n):
        if(a1[i]==a2[j]):
            array1.append(abs(i-j))
min1=min(array1)
ind=[]
for i in range(0,n):
    if(array1[i]==min1):
        ind.append(i)
max1=[]
len1=len(ind)
for i in range(0,len1):
    max1.append(a1[ind[i]])
print(min(max1))