from datetime import datetime

formatting = "%a %d %b %Y %H:%M:%S %z"
n = int(input())

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
