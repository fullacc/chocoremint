s = input().split(' ')
print(*[x[0].upper() + x[1:] for x in s])
