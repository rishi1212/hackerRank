N, K = map(int, input().split())
T = map(int, input().split())

cnt = 0
i = 0
j = 1
m = 1

while i < N:
    if m <= j and j <= min(m + K - 1, T[i]):
        cnt += 1
    j += 1
    m += K
    if m > T[i]:
        i += 1
        m = 1
print(cnt)
