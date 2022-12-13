import numpy as np

with open('inputs/inputday9.txt') as f:
    data = f.read().splitlines()
    
for i in range(len(data)):    
    data[i] = data[i].split(' ')

def steps(dir, num, head, tail):
    for i in range(num):
        if dir == 'R':
            head = [head[0] + 1, head[1]]
            if head[0] - tail[0] == 2:              
                tail = [head[0] - 1, head[1]]
                tail_list.append(tail)
        elif dir == 'L':
            head = [head[0] - 1, head[1]]
            if head[0] - tail[0] == -2: 
                tail = [head[0] + 1, head[1]]
                tail_list.append(tail)
        elif dir == 'U':
            head = [head[0], head[1] + 1]
            if head[1] - tail[1] == 2: 
                tail = [head[0], head[1] - 1]
                tail_list.append(tail)
        elif dir == 'D':
            head = [head[0], head[1] - 1]
            if head[1] - tail[1] == -2: 
                tail = [head[0], head[1] + 1]
                tail_list.append(tail)
    return head, tail

def move_head(dir, head):
    if dir == 'R':
        head = [head[0] + 1, head[1]]
    elif dir == 'L':
        head = [head[0] - 1, head[1]]
    elif dir == 'U':
        head = [head[0], head[1] + 1]
    elif dir == 'D':
        head = [head[0], head[1] - 1]
    return head

def steps_knots(head, tail):        
    if head[0] - tail[0] == 2:
        if head[1] - tail[1] == 2:
            tail = [head[0] - 1, head[1] - 1]
        elif head[1] - tail[1] == -2:
            tail = [head[0] - 1, head[1] + 1]
        else:              
            tail = [head[0] - 1, head[1]]
    elif head[0] - tail[0] == -2: 
        if head[1] - tail[1] == 2:
            tail = [head[0] + 1, head[1] - 1]
        elif head[1] - tail[1] == -2:
            tail = [head[0] + 1, head[1] + 1]
        else:
            tail = [head[0] + 1, head[1]]
    elif head[1] - tail[1] == 2: 
        tail = [head[0], head[1] - 1]
    elif head[1] - tail[1] == -2: 
        tail = [head[0], head[1] + 1]
    return tail

# Part 1

tail = [0, 0]
head = [0, 0]
tail_list = [tail]
for i in range(len(data)):
    head, tail = steps(data[i][0], int(data[i][1]), head, tail)

print(len(np.unique(tail_list, axis=0)))

# Part 2

tail_list = [[0, 0]]
knot_list = [[0, 0] for i in range(10)]
for i in range(len(data)):
    for j in range(int(data[i][1])):      
        for k in range(len(knot_list)):
            if k == 0:
                knot_list[k] = move_head(data[i][0], knot_list[k])
            else:
                knot_list[k] = steps_knots(knot_list[k-1], knot_list[k])
            tail_list.append(knot_list[-1])

print(len(np.unique(tail_list, axis=0)))