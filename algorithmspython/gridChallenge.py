a = [[list(input().strip()) for _ in range(int(input()))] for _ in range(int(input()))]
for i in a:
    i = list(map(sorted, i))
    i = [[i[x][y] <= i[x + 1][y] for x in range(len(i) - 1)] for y in range(len(i))]
    i = all([all(i[m]) for m in range(len(i))])
    print('YES' if i == True else 'NO')
