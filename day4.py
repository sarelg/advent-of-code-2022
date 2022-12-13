import numpy as np
import re

def parser(line):
    line = re.split('-|,', line)
    return line

def contain(a, b, c, d):
    if a >= c and b <= d:
        return True
    elif c >= a and d <= b:
        return True
    else:
        return False

def contain2(a, b, c, d):
    if a >= c and a <= d:
        return True
    elif c >= a and c <= b:
        return True
    else:
        return False

with open('inputday4.txt') as f:
    data = f.read().splitlines()
    
elf_list = []
for line in data:    
    nums = parser(line)
    elf_list.append(contain2(int(nums[0]), int(nums[1]), int(nums[2]), int(nums[3])))

print(sum(elf_list))



