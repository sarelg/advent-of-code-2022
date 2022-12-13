import numpy as np

with open("inputs\inputday6.txt") as f:
    data = f.read()

for i in range(14,int(len(data))):
    tmp = data[i - 14:i]
    tmp1 = np.unique(list(tmp))
    if len(tmp1) == 14:
        print(tmp)
        print(i)
        break
