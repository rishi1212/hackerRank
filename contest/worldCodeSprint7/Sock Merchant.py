from collections import Counter

n = int(input())
c = Counter(map(int, input().split()))
ans = 0

for x in c:
    ans += c[x] // 2

print(ans)