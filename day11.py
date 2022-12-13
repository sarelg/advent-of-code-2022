import numpy as np
import re
from tqdm import tqdm
import math

class monkey:
    def __init__(self, items, operation, test, if_true, if_false):
        self.items = items
        self.operation = operation
        self.if_true = if_true
        self.if_false = if_false
        self.test = test
    
    def inspect(self, divisor):
        item = self.items[0]
        oper = self.operation.split()
        if oper[1] == 'old':
            if oper[0] == '*':
                item *= item
            elif oper[0] == '+':
                item += item
        else:
            if oper[0] == '*':
                item *= int(oper[1])
            elif oper[0] == '+':
                item += int(oper[1])
        item %= divisor
        if np.mod(item, self.test) == 0:
            self.items = self.items[1:]
            return item, int(self.if_true)
        else:
            self.items = self.items[1:]
            return item, int(self.if_false)

with open('inputs/inputday11.txt') as f:
    lines = f.read().strip().splitlines()

monkeys = []
for line in lines:
    line = line.strip()
    if line[0:6] == 'Monkey':
        num = line[7:-1]
    elif line[0:3] == 'Sta':
        items = re.split(':|,', line[14:])
        items = [int(i.strip()) for i in items[1:]]
    elif line[0:3] == 'Ope':
        operation = line[21:]
    elif line[0:3] == 'Tes':
        test = int(line[19:])
    elif line[0:4] == 'If t':
        if_true = line[-1]
    elif line[0:4] == 'If f':
        if_false = line[-1]
        monkeys.append(monkey(items, operation, test, if_true, if_false))

# print(monkeys[0].inspect())

divisor = math.lcm(*[monkey.test for monkey in monkeys])

tot_inspected = [0]*len(monkeys)
rounds = 10000
for i in tqdm(range(rounds)):
    for j, monkey in enumerate(monkeys):
        for item in monkey.items:
            item, new_monkey = monkey.inspect(divisor)
            tot_inspected[j] += 1
            monkeys[new_monkey].items.append(item)

# for monkey in monkeys:
#     print(monkey.items)

for i in range(len(monkeys)):
    print(f'Monkey {i} inspected items {tot_inspected[i]} times')

sorted = np.sort(tot_inspected)
print(f'monkey business = {float(sorted[-1])*float(sorted[-2])}')
