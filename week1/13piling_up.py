from collections import deque
import math


def try_build(stack, block=math.inf):
    if not stack:
        return True
    if stack[0] > stack[-1]:
        if stack[0] <= block:
            block = stack[0]
            stack.popleft()
            return try_build(stack, block)
        else:
            return False
    else:
        if stack[-1] <= block:
            block = stack[-1]
            stack.pop()
            return try_build(stack, block)
        else:
            return False


n = int(input())
for i in range(n):
    m = int(input())
    lengths = input().split(" ")
    lengths = deque([int(x) for x in lengths])
    if try_build(lengths):
        print("Yes")
    else:
        print("No")
