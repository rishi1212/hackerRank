N,n = int(raw_input()),raw_input().split()
print all([int(i)>0 for i in n]) and any([j == j[::-1] for j in n])