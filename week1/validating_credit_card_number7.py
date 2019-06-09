import sys
import re


def validate():
    reg = re.compile(r"^" r"(?!.*(\d)(-?\1){3})" r"[456]" r"\d{3}" r"(?:-?\d{4}){3}" r"$")
    res = []
    n = int(sys.stdin.readline())

    for i in range(0, n):
        s = sys.stdin.readline()
        print("Valid" if reg.search(s) else "Invalid")
        res.append("Valid" if reg.search(s) else "Invalid")
    return res
def main():
    validate()

if __name__ == '__main__':
    main()