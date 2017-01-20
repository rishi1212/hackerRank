from itertools import product
K,M = map(int, input().split())
seqs = [set(map(lambda x: (int(x)*int(x))%M, raw_input().split()[1:])) for i in range(K)]
sum_list = [sum(x)%M for x in product(*seqs)]
print(max(sum_list))
