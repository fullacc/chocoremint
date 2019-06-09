from collections import Counter

n = int(input())
lines = []

for i in range(n):
    lines.append(input())
result = list(Counter(lines).items())
print(len(result))
for i in result:
    print(i[1], end=" ")
