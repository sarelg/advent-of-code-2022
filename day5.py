import numpy as np
import csv

def move_function(items, sack1, sack2):
    sack1 = sack1 - 1
    sack2 = sack2 - 1
    for i in range(items):
        res[sack2].append(res[sack1][-1])
        res[sack1].pop()

def move_function2(items, sack1, sack2):
    sack1 = sack1 - 1
    sack2 = sack2 - 1
    res[sack2].extend(res[sack1][-items:])
    res[sack1] = res[sack1][:-items]

with open('stacksday5.txt') as f:
    data = f.read().splitlines()
    res = [[] for i in range(9)]
    for index, line in enumerate(data):
        for i in range(0, 9):
            val = line[i*4 + 1]
            if val != ' ':
                res[i].append(val)

    for i in range(len(res)):    
        res[i].reverse()
    
with open('actionsday5.txt') as f:
    data = f.read().splitlines()
    for line in data:
        line = line.split(' ')
        move_function2(int(line[1]), int(line[3]), int(line[5]))       

fin = []    
for l in res:
    fin.append(l[-1])

print(''.join(fin))