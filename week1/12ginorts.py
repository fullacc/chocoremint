import re

to_sort = input()

lower_case = re.findall(r"[a-z]", to_sort)
upper_case = re.findall(r"[A-Z]", to_sort)

numbers = re.findall(r"[0-9]", to_sort)

evens = []
odds = []

for i in numbers:
    if int(i) % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

lower_case.sort()
upper_case.sort()
odds.sort()
evens.sort()

result = "".join(x for x in lower_case + upper_case + odds + evens)
print(result)
