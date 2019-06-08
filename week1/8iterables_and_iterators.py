import itertools
import sys

n = int(sys.stdin.readline())

s = sys.stdin.readline().strip().replace(" ", "")

m = int(sys.stdin.readline())

combinations = list(itertools.combinations(s, m))

combinations_with_a = 0

for i in combinations:
    if 'a' in i:
        combinations_with_a += 1

print(combinations_with_a/len(combinations))
