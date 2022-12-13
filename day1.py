import numpy as np

with open('input.txt') as f:
    data = f.read().splitlines()

totals = [0]
for line in data:
    if line != '':
        totals[-1] = totals[-1] + int(line)
    else:
        totals.append(0)

# print(np.max(totals))

sorted = np.sort(totals)[::-1]

top_three = np.sum(sorted[:3])

print(top_three)