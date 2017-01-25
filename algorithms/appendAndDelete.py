s = input().strip()
t = input().strip()
k = int(input().strip())

length1 = len(s)
length2 = len(t)

length = length1 if length1 <= length2 else length2
count = 0

for i in range(length):
    if s[i] == t[i]:
        count += 1
    else:
        break

deletions = length1 - count
additions = length2 - count

operations = deletions + additions

doubled = 0
if s == t:
    doubled = (length1 * 2) + 1

if (((length1 == length2) or (length1 > length2)) and operations <= k) \
        or doubled == k or (s.count(s[0]) == length1 and t.count(t[0]) == length2):
    print ('Yes')
else:
    print ('No')