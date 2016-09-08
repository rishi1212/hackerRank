from collections import namedtuple
test_count = int(input())
fields = ",".join(input().split(' '))
Grade = namedtuple('Grade', fields)
sum = 0
for i in range(test_count):

    hede = input().strip().split()
    grade = Grade(*hede)
    sum += int(grade.MARKS)

print(sum/test_count)