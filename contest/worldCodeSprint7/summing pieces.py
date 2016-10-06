def coeff(n):
    a = pow(2, n, 1000000007)
    res = [a - 1]
    for i in range((n - 1) // 2):
        a = a * 250000002 % 1000000007
        res.append((res[-1] + (a - 1) * pow(2, i, 1000000007)) % 1000000007)
    if n & 1:
        return res + res[-2::-1]
    return res + res[::-1]

print(sum(map(lambda x, y: x * y % 1000000007, coeff(int(input())), map(int, input().split()))) % 1000000007)