import re

m = int(raw_input())
for i in range(0,m):
    temp = raw_input()
    print bool(re.match(r"^[-+]?[0-9]*\.[0-9]+$",temp))
