from collections import deque
import math


def try_build(stack, block=math.inf):
    while stack:
        if stack[0] > stack[-1]:
            if stack[0] <= block:
                # print(stack[0])
                block = stack[0]
                stack.popleft()
            else:
                return False
        else:
            if stack[-1] <= block:
                # print(stack[-1])
                block = stack[-1]
                stack.pop()
            else:
                return False
    return True


n = int(input())
for i in range(n):
    m = int(input())
    lengths = input().split(" ")
    lengths = deque([int(x) for x in lengths])
    if try_build(lengths):
        print("Yes")
    else:
        print("No")
