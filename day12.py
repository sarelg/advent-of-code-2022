import numpy as np
import pandas as pd
import sys

sys.setrecursionlimit(10000)

class cell:
    def __init__(self, i, j, value):
        self.i = i
        self.j = j
        if value == 'S':
            self.value = 0
        else:
            self.value = value  
        self.pre_value = value

    def __repr__(self):
        i = self.i
        j = self.j
        return str(self.pre_value)
   
    def get_neighbors(self):
        neighbors = []
        dir_dict = {'u': (-1, 0), 'd': (1, 0), 'r': (0, 1), 'l': (0, -1)}
        for direction in dir_dict:
            i = self.i + dir_dict[direction][0]
            j = self.j + dir_dict[direction][1]
            try:
                if df.iloc[i, j].value - self.value <= 1: 
                    neighbors.append(df.iloc[i, j])
            except (IndexError):
                pass
            except:
                if df.iloc[i, j].value == 'E':
                    neighbors.append(df.iloc[i, j])
        self.neighbors = neighbors  

    def get_path(self, history, end):
        path = []
        num_steps = 0
        path = [[] for i in range(len(self.neighbors))]
        for i in range(len(self.neighbors)):
            path[i].append(self.value)
            if self.neighbors[i].value == end:
                path.append(self.neighbors[i].value)
                break
            else:
                if (self.neighbors[i].i, self.neighbors[i].j) in history:
                    continue
                else:
                    history.append((self.neighbors[i].i, self.neighbors[i].j))
                    # path.append(self.neighbors[i])
                    path[i].extend(self.neighbors[i].get_path(history, end)[0])
        return path, num_steps

def create_grid(df):
    for i in range(len(df)):
        for j in range(len(df.iloc[i])):
            df.iloc[i, j] = cell(i, j, df.iloc[i, j])


def get_neighbors():
    for i in range(len(df)):
        for j in range(len(df.iloc[i])):
            df.iloc[i, j].get_neighbors()


if __name__ == '__main__':
    with open('inputs\day12example.txt', 'r') as f:
        lines = f.read().splitlines()

    letter_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25}

    for i, line in enumerate(lines):
        lines[i] = list(line)
        for j in range(len(lines[i])):
            if lines[i][j] in letter_dict:
                lines[i][j] = letter_dict[lines[i][j]]
        
    df = pd.DataFrame(lines)   

    create_grid(df)
    get_neighbors()
    # print(df)
    # print(df.iloc[21, 0])

    history = []
    start = np.where(np.array(lines) == 'S')
    path, num = df.iloc[start[0][0], start[1][0]].get_path(history, 'E')
    print(path)
# def step(i, j, history, num_steps):
#     possible_steps = []
#     for option in options:
    
#     print(df)
