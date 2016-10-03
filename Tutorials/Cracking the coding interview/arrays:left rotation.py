def array_left_rotation(a, n, k):
    ans=[]
    ans=a[k:]
    ans1=(a[:k])
    ans=ans+ans1
    return ans


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(answer)
