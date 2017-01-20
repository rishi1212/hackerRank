import re

m = int(input())
for i in range(0,m):
    temp = input()
    print bool(re.match(r"^[-+]?[0-9]*\.[0-9]+$",temp))
