from collections import defaultdict

n, m, k = map(int, input().split())

tracks = defaultdict(list)
for _ in range(k):
    row, c1, c2 = map(int, input().split())
    tracks[row].append((c1, -1))
    tracks[row].append((c2 + 1, 1))

ans = 0
for row in tracks:
    tracks[row].sort()

    prev = tracks[row][0][0]
    depth = 1
    for event in tracks[row][1:]:
        if depth > 0:
            ans += (event[0] - prev)

        depth -= event[1]
        prev = event[0]

print(n * m - ans)
