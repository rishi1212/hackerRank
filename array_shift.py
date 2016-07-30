#left rotation
#python 3.0
l1=list(map(int,input().split(" ")))
n=l1[0]
d=l1[1]
array=list(map(int,input().split(" ")))
new_array=[]
for i in range(d,n):
    new_array.append(array[i])
for i in range(0,d):
    new_array.append(array[i])
for i in new_array:
    print(i,end=" ")
