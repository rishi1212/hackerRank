from collections import OrderedDict

number_ = int(input())
odict = OrderedDict()
for i in range(number_):
    litem = input().split(' ')
    price = int(litem[-1])
    item_name = " ".join(litem[:-1])
    if odict.get(item_name):
        odict[item_name] += price
    else:
        odict[item_name] = price

for i,v in odict.items():
    print(i,v)