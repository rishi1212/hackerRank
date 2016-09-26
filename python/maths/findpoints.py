t=int(input())
for i in range(0,t):
    a=list(map(int,input().split(" ")))
    x1=a[0]
    x2=a[2]
    y1=a[1]
    y2=a[3]
    print((2*x2-x1),(2*y2-y1))