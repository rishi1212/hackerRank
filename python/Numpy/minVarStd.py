import numpy as np
n,_=map(int,input().split())
a=np.array([list(map(int,input().split())) for _ in range(n)])
print(np.mean(a,axis=1),np.var(a,axis=0),np.std(a),sep='\n')