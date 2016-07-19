a=input().strip()
la=list(map(int,a.split(" ")))
array=list(map(int,input().split(" ")))
n=la[0]
k=la[1]
q=la[2]
array1=[]
for i in range(n-k,n):
    array1.append(array[i])
for i in range(0,n-k):
    array1.append(array[i])
for i in range(0,q):
    query=int(input())
    print(array1[query])

