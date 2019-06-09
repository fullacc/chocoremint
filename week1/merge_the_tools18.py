import textwrap
from collections import OrderedDict


def merge_the_tools(s, k):
    s = textwrap.wrap(s, k)
    for i in s:
        for j in OrderedDict.fromkeys(i):
            print(j, end="")
        print()


if __name__ == "__main__":
    s, k = input(), int(input())
    merge_the_tools(s, k)
