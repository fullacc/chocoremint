import itertools
import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip().replace(" ","")
m = int(sys.stdin.readline())
com = list(itertools.combinations(s,m))
b = 0

for i in com:
	if 'a' in i:
		b+=1

print(b/len(com))
