s="hello"
ans=[]
for i in range(len(s)-1,-1,-1):
    ans.append(s[i])
print("".join(ans))