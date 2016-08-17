n1=list(map(int,input().split(" ")))
n=n1[0]
d=n1[1]
array=list(map(int,input().split(" ")))
count=0
for i in range(0,n):
    cache=[]
    cache.append(array[i])
    cache.append(array[i]+d)
    cache.append(array[i]+(2*d))
    if(cache[0] in array and cache[1] in array and cache[2] in array):
        count+=1
print(count)