if __name__ == "__main__":
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    arr.sort(key=lambda x: x[k], reverse=False)

    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
