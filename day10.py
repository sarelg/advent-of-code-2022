import numpy as np


def read_input(filename):
    with open(filename) as f:
        return f.read().splitlines()


def doop(inst, clock, X):
    if inst[0:4] == 'noop':
        clock += 1
        log.append([clock, X])
    elif inst[0:4] == 'addx':
        for i in range(2):
            num = int(inst[5:])
            clock += 1
            if i == 1:
                X += num
            log.append([clock, X])

def signal_strength(log, cycle):
    return log[cycle-1][1] * cycle


def draw(crt, reg):
    if crt == reg or crt == reg+1 or crt == reg-1:
        return '#'
    else:
        return ' '


data = read_input('inputs/inputday10.txt')

# Part 1

clock = 1
X = 1
log = [[clock, X]]
for line in data:
    doop(line, log[-1][0], log[-1][1])


tot_strength = 0
cycles = [40*i + 20 for i in range(6)]
for cycle in cycles:
    strength = signal_strength(log, cycle)
    tot_strength += strength

print(tot_strength)

# Part 2

new_log = log

line_list = [[] for i in range(6)]
for i in range(6):
    for j in range(40):
        line_list[i].append(draw(j, new_log[i*40+j][1]))

for i in range(6):
    print('  '.join([item for item in line_list[i]]))
