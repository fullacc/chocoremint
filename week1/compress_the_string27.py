import itertools

s = input()
result = [(len(list(g)), k) for k, g in itertools.groupby(s)]

for i in result:
    print("(" + str(i[0]) + ", " + i[1] + ")", end=" ")
