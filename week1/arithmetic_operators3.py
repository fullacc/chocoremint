def count():
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
    return a+b, a-b, a*b
if __name__ == '__main__':
    count()