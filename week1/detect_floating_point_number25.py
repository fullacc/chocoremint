import re

n = int(input())
for i in range(n):
    s = input()
    if re.match(r"^[-+]?[0-9]*\.[0-9]+$", s) is not None:
        print("True")
    else:
        print("False")
