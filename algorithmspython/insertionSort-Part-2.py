n = int(input())
a = [int(x) for x in input().split(' ')]
def printArr(arr):
    s = '' #NO SPACE
    for i in range(len(arr)):
        s = s+ str(arr[i])
        if (i < len(arr) -1):
            s = s + ' '
    print (s)
for i in range(1,n):
    for j in range(i):
        if (a[i-j] < a[i-j-1]):#if(a[i]<a[j])
            t = a[i-j]			#t=a[i]
            a[i-j] = a[i-j-1]	#a[i]=a[j]
            a[i-j-1] = t		#a[j]=t
    printArr(a)