from collections import defaultdict


nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = defaultdict(list)
for i in range(n):
    arr[input()].append(i + 1)

for j in range(m):
    s = input()
    if s in arr:
        print(*arr[s])
    else:
        print("-1")
