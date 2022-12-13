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


def find_dirs(data):
    dirs = []
    for line in data:
        if line[0:3] == 'dir':
            dirs.append(line[4:])
    return dirs


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
    
def check_name(name, dirs):
    if name in dirs:
        name = name + '_'
        name = check_name(name, dirs)
    return name

curr_dir = ''
file_struc = []
dirs = []
for line in data:
    if line[0:4] == '$ cd' and line[5:] != '..':
        if line[5:] in dirs:
            curr_dir = check_name(line[5:], dirs)
        else:
            curr_dir = line[5:]
        dirs.append(curr_dir)
        prev_dir = curr_dir
    elif line[0:4] == '$ ls':
        continue
    elif line[5:] == '..':
        curr_dir = prev_dir
    elif line[5:] != '..':
        if line[0:3] == 'dir':
            if line[4:] in dirs:
                line = check_name(line[4:], dirs)
                line = 'dir ' + line
                file_struc.append(curr_dir + '/' + line)
            else:
                file_struc.append(curr_dir + '/' + line)
        else:
            file_struc.append(curr_dir + '/' + line)


list_all = [[] for i in range(len(dirs))]
for item in file_struc:
    ind = dirs.index(item[0:item.rfind('/')])
    list_all[ind].append(item[item.rfind('/')+1:])

all_counts = []
for i, item in enumerate(list_all):
    files = unpack(item)
    if i == 0:
        root_files = files
    all_counts.append(count(files))
    # print(dirs[i], count(files))

free = 70000000 - mem

needed = 30000000 - free
print(needed)

del_poss = [x for x in all_counts if x > needed]
print(np.sort(del_poss))
# not_in = [x for x in files_ if x not in root_files]
# print(len(not_in))
# print(sum(del_poss))
# print(list_all)
# print('\n')
# print(mem-all_counts[0])

# files = unpack(list_all[0])
# print(files)
