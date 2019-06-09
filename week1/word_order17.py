from collections import Counter


def word_order():
    n = int(input())
    lines = []
    res = []
    for i in range(n):
        lines.append(input())
    result = list(Counter(lines).items())
    print(len(result))
    res.append(len(result))
    tempres = []
    for i in result:
        print(i[1], end=" ")
        tempres.append (i[1])
    res.append(tempres)
    return res


def main():
    word_order()


if __name__ == '__main__':
    main()
