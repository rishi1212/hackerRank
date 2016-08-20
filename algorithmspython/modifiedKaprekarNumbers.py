def checkIsKaprekar( num ):
    if(num==1):
        return True
    elif((num**2)<15):
        return False
    string_num = str(num**2)
    if num == int(string_num[:len(string_num)//2]) + int(string_num[len(string_num)//2:]):
        return True
p=int(input())
q=int(input())
number=[]
for i in range(p,q+1):
    if(checkIsKaprekar(i)==True):
        number.append(i)

if(len(number)>0):
    for i in number:
        print(i,)
else:
    print("INVALID RANGE")