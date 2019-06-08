n = int(input())
used = 0
if n % 2 == 1:
    used = 1
else:
    if n > 5 and n < 21:
        used = 1

if used == 1:
    print("Weird")
else:
    print("Not Weird")
