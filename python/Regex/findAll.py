import re


str1 = raw_input()
consonants='qwrtypsdfghjklzxcvbnm'
vowels='aeiou'
m = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',str1,flags = re.I)
if not m:
    print "-1"
else:
    for i in m:
        print i