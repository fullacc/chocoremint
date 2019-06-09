import re


def matr():
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    matrix = []

    s = ""

    for _ in range(n):
        matrix_item = input()
        matrix.append(matrix_item)

    for i in range(0, m):
        for j in range(0, n):
            s = s + matrix[j][i]

    print(re.sub(r"(?<=([A-Za-z0-9]))([^A-Za-z0-9]+)(?=([A-Za-z0-9]))", " ", s))
    return re.sub(r"(?<=([A-Za-z0-9]))([^A-Za-z0-9]+)(?=([A-Za-z0-9]))", " ", s)


def main():
    matr()


if __name__ == "__main__":
    main()
