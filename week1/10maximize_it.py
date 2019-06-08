from itertools import product

nm = input().split()

n = int(nm[0])

m = int(nm[1])

matrix = []

s = ""
answer = 0

for _ in range(n):
    matrix_item = input()

    matrix_item = matrix_item[2:]
    matrix_item = matrix_item.split(" ")

    item = [abs(int(s)) for s in matrix_item]
    matrix.append(item)
results = map(lambda x: sum(i ** 2 for i in x) % m, product(*matrix))
print(max(results))
