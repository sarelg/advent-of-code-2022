import numpy as np
import sys

# sys.setrecursionlimit(10**6)

with open('inputs\inputday7.txt') as f:
    data = f.read().splitlines()

# with open('inputs\day7example.txt') as f:
#     data = f.read().splitlines()

def find_mem(data):
    mem = 0
    files = []
    for line in data:
        if line[0].isnumeric():
            mem += int(line[0:line.find(' ')])
            files.append(line)
    return mem, files
mem, files_ = find_mem(data)
# print(mem)

def check_name(name, dirs):
    if name in dirs:
        name = name + '_'
        name = check_name(name, dirs)
    return name


def find_dirs(data):
    dirs = ['/']
    for line in data:
        if line[0:3] == 'dir':
            if line[4:] in dirs:
                dirs.append(check_name(line[4:], dirs))
            else:
                dirs.append(line[4:])
    return dirs

print(find_dirs(data))


def unpack(dir):
    files = []
    for item in dir:
        if item[0:3] == 'dir':
            ind = dirs.index(item[4:])
            files.extend(unpack(list_all[ind]))
        else:
            files.append(item)
    return files

def count(files):
    count = 0
    for item in files:
        count += int(item.split(' ')[0])
    return count
    


curr_dir = ''
file_struc = []
# dirs = []
# for line in data:
    
# print(sum(del_poss))
# print(list_all)
# print('\n')
# print(mem-all_counts[0])

# files = unpack(list_all[0])
# print(files)
