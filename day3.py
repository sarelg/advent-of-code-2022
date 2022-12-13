import numpy as np

with open('inputday3.txt') as f:
    data = f.read().splitlines()

comm_list = []
for line in data:
    length = len(line)
    comp1 = line[0:int(length/2)]
    comp2 = line[int(length/2):length]
    comm_list.append([char for char in comp1 if char in comp2])
    comm_list[-1] = comm_list[-1][0]

az_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

pri_list = []
for char in comm_list:
    pri_list.append(az_list.index(char)+1)

print(np.sum(pri_list))

comm_list2 = []
for i in range(0, int(len(data)/3)):
    comm_list2.append([char for char in data[i*3] if char in data[i*3+1] and char in data[i*3+2]])
    comm_list2[-1] = comm_list2[-1][0]

pri_list2 = []
for char in comm_list2:
    pri_list2.append(az_list.index(char)+1)

print(np.sum(pri_list2))