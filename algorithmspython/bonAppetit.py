l1=list(map(int,input().split(" ")))
l2=list(map(int,input().split(" ")))
bCharged=int(input())
n=l1[0]
skip=l1[1]
sum1=0
for i in range(0,n):
    if(i!=skip):
        sum1+=l2[i]
bActual=sum1/2
if(bCharged==bActual):
    print("Bon Appetit")
else:
    print(int(bCharged-bActual))