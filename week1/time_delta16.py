from datetime import datetime


def timedelta():
    formatting = "%a %d %b %Y %H:%M:%S %z"
    n = int(input())
    res = []
    for i in range(n):
        result = int(
            abs(
                (
                    datetime.strptime(input(), formatting)
                    - datetime.strptime(input(), formatting)
                ).total_seconds()
            )
        )
        print(result)
        res.append(result)
    return res


def main():
    timedelta()


if __name__ == '__main__':
    main()