import numpy as np
N = int(raw_input().strip())
a, b = [np.array([raw_input().strip().split() for i in xrange(N)], int) for j in xrange(2)]
print np.mat(a) * np.mat(b)