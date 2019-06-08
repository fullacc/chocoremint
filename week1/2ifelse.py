n = int(input())
u = 0
if n%2== 1:
    u=1
else:
    if n>5 and n<21:
        u=1

if u==1:
    print("Weird")
else:
    print("Not Weird")
