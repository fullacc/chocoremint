def printf():
    n = int(input())
    j = ""
    for i in range(n):
        j = j + str(i + 1)
    print(j)
    return j


def main():
    printf()


if __name__ == '__main__':
    main()
