print("\n".join(map(lambda x: "First" if ((int(x[0]) - 1) // 2 % 2) or ((int(x[1]) - 1) // 2 % 2) else "Second", (input().split() for _ in range(int(input()))))))