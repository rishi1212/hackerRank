import sys

arr = []
for arr_i in range(6):
  arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
  arr.append(arr_t)

hrgls_sum = []
count = 0

for i in range(4):
    for j in range(4):
        hrgls_sum.append(sum(arr[i][j:j+3]) + int(arr[i+1][j+1]) + sum(arr[i+2][j:j+3]))

print(max(hrgls_sum))