def main():
    n = int(input())

    for i in range(0, n):
        print(i*i)
    return [i*i for i in range(0,n)]
if __name__ == '__main__':
    main()