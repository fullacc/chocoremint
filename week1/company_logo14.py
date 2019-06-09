from collections import Counter
from operator import itemgetter

words = input()
words = sorted(words)
result = Counter(words).most_common(3)
result.sort(key=lambda x: (-x[1], x[0]))
for i in result:
    print(i[0], i[1])
