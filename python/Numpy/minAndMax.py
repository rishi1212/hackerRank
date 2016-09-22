import numpy

N = input()
M = int(N[0])

myArray = []

for i in range(M):
    pill = input().split()
    for x in pill:
        indx = pill.index(x)
        x = int(x)
        pill[indx] = x
    myArray.append(pill)

minArray = numpy.min(myArray, axis = 1)
print(numpy.max(minArray))