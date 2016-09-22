m, n, r = [int(i) for i in raw_input().strip().split(' ')]

mat = [[int(i) for i in raw_input().strip().split(' ')] for _ in xrange(m)]

def printMat(mat):
    for row in mat:
        for elem in row:
            print elem,
        print

def rotateMatrix(matr, r):
    offset = 0
    while n - offset > n / 2 and m - offset > m / 2:
        top = [(offset, i) for i in range(offset, n - offset, 1)]
        right = [(i, n - 1 - offset) for i in range(offset + 1, m - 1 - offset, 1)]
        bot = [(m - 1 - offset, i) for i in range(n - 1 - offset, offset - 1, -1)]
        left = [(i, offset) for i in range(m - offset - 2, offset, -1)]
        idx = top + right + bot + left

        circle = [matr[p[0]][p[1]] for p in idx]

        rMod = r % len(circle)

        circle = circle[rMod:] + circle[0:rMod]

        for q in range(len(idx)):
            index = idx[q]
            matr[index[0]][index[1]] = circle[q]

        offset += 1

    return matr

printMat(rotateMatrix(mat, r))