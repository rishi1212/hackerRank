# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
# Check proper contents/starting/count w/o hypen
normal = r'^([4-6])([0-9]){15}$'
# Proper contents/separation/count with hypen
special = r'^([4-6][0-9]{3})-([0-9]{4})-([0-9]{4})-([0-9]{4})$'
# Match any string w/o 4 non-unique chars
repeating = r'^(?:(.)(?!-*\1-*\1-*\1))*$'

reg = map(re.compile, [normal, repeating])
spc = map(re.compile, [special, repeating])
for _ in range(int(input())):
    l = input().strip()
    if l.find('-') >=0:
        tests = map(bool,[x.match(l) for x in spc])
    else:
        tests = map(bool,[x.match(l) for x in reg])
    print 'Valid' if all(tests) else 'Invalid'