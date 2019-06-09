from collections import namedtuple
import statistics

n = int(input())
columns = input().split()
Tuple = namedtuple("Tuple", columns)
res = []
for i in range(n):
    s = input().split()
    res.append(int(Tuple._make(s).MARKS))
print(statistics.mean(res))
