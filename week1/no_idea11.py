nm = input().split()

n = int(nm[0])

m = int(nm[1])

to_analyze = input().split(" ")

happy = set(input().split(" "))
unhappy = set(input().split(" "))

answer = 0

for i in to_analyze:
    if i in happy:
        answer += 1
    elif i in unhappy:
        answer -= 1

print(answer)
