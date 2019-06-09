import re


def toand(match):
    return " and "


def toor(match):
    return " or "


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s = input()
        s = re.sub(r" \|\| ", toor, re.sub(r" \&\& ", toand, s))
        print(re.sub(r" \|\| ", toor, re.sub(r" \&\& ", toand, s)))
