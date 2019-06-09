n = int(input())
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
result = list(map(lambda x: x ** 3, fibonacci))
print(result[:n])
