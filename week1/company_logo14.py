from collections import Counter
from operator import itemgetter


def company_logo():
    res = []
    words = input()
    words = sorted(words)
    result = Counter(words).most_common(3)
    result.sort(key=lambda x: (-x[1], x[0]))
    for i in result:
        print(i[0], i[1])
        res.append([i[0], i[1]])
    return res


def main():
    company_logo()


if __name__ == '__main__':
    main()
