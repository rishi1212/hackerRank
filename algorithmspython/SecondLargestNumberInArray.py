#input an array
a=raw_input().split(" ")
array=list(map(int,a))
f,s=0,0
f=array[0]
s=array[1]
for i in range(2,len(array)):
    if(array[i]>f and array[i]>s):
        s=f
        f=array[i]
    elif(array[i]<f and array[i]>s):
        s=array[i]
    elif(array[i]>f and array[i]<s):
        s=f
        f=array[i]
if(s>f):
    temp=s
    s=f
    f=temp

print(s,f)

