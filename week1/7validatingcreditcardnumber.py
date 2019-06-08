import sys
import re

reg = re.compile(
	r"^"
    r"(?!.*(\d)(-?\1){3})"
    r"[456]"
    r"\d{3}"
    r"(?:-?\d{4}){3}"
    r"$"
	)

n = int(sys.stdin.readline())

for i in range (0,n):
	s = sys.stdin.readline()
	print("Valid" if reg.search(s) else "Invalid")
