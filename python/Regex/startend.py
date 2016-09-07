s, k = input(), input()
if not [print((i, i + len(k) - 1)) for i in range(len(s) - len(k)) if k in s[i:i + len(k)]]:
    print((-1, -1))