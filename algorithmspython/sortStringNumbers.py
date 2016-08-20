a=['1','2','3','0','9']
number=[]
for i in a:
    number.append(ord(i))
number.sort(reverse = True)
for i in number:
    print (chr(i))