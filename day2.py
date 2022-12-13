import numpy as np


def rock_paper_scissors(a, b):  
    if a == 'A' and b == 'X':
        return (1 + 3)
    elif a == 'A' and b == 'Y':
        return (2 + 6)
    elif a == 'A' and b == 'Z':
        return (3)
    elif a == 'B' and b == 'X':
        return (1)
    elif a == 'B' and b == 'Y':
        return (2 + 3)
    elif a == 'B' and b == 'Z':
        return (3 + 6)
    elif a == 'C' and b == 'X':
        return (1 + 6)
    elif a == 'C' and b == 'Y':
        return (2)
    elif a == 'C' and b == 'Z':
        return (3 + 3)

def rock_paper_scissors_other_way(a, b):  
    if a == 'A' and b == 'X':
        return (3)
    elif a == 'A' and b == 'Y':
        return (1 + 3)
    elif a == 'A' and b == 'Z':
        return (2 + 6)
    elif a == 'B' and b == 'X':
        return (1)
    elif a == 'B' and b == 'Y':
        return (2 + 3)
    elif a == 'B' and b == 'Z':
        return (3 + 6)
    elif a == 'C' and b == 'X':
        return (2)
    elif a == 'C' and b == 'Y':
        return (3 + 3)
    elif a == 'C' and b == 'Z':
        return (1 + 6)

with open('inputday2.txt') as f:
    data = f.read().splitlines()

total = 0
total2 = 0
for round in data:
    total += rock_paper_scissors(round[0], round[2])
    total2 += rock_paper_scissors_other_way(round[0], round[2])

print(total)
print(total2)




