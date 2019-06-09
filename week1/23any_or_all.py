n, s = input(), input().split(" ")
print("True") if all([int(i) > 0 for i in s]) and any(
    [(i == i[::-1]) for i in s]
) else print("False")
