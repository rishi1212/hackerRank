a=0
b=1
fib=[]
fib.append(a)
fib.append(b)
for i in range(0,10000):
    c=a+b
    a=b
    b=c
    fib.append(c)
t=int(input())
for i in range(0,t):
    number=int(input())
    if(number in fib):
        print("IsFibo")
    else:
        print("IsNotFibo")