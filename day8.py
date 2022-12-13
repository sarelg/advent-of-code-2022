import numpy as np
import pandas as pd


with open('inputs\inputday8.txt', 'r') as f:
    lines = f.read().splitlines()

# with open('inputs\day8example.txt', 'r') as f:
#     lines = f.read().splitlines()

for i, line in enumerate(lines):
    lines[i] = list(line)

df = pd.DataFrame(lines)


def is_visible(i, j):
    max_row_left = np.max(df.iloc[i, 0:j])
    max_col_top = np.max(df.iloc[0:i, j])
    max_row_right = np.max(df.iloc[i, j+1:])
    max_col_bottom = np.max(df.iloc[i+1:, j])
    if df.iloc[i, j] > max_row_left or df.iloc[i, j] > max_col_top or df.iloc[i, j] > max_row_right or df.iloc[i, j] > max_col_bottom:
        return True
    else:
        return False


# need the first one taller than me
def scenic_score(i, j):
    max_col_top = np.where(df.iloc[0:i, j] >= df.iloc[i, j])[0]
    if len(max_col_top) == 0:
        max_col_top = 0
    else:
        max_col_top = max_col_top[-1]
    
    max_col_bottom = np.where(df.iloc[i+1:, j] >= df.iloc[i, j])[0]
    if len(max_col_bottom) == 0:
        max_col_bottom = len(df.index) - 1
    else:
        max_col_bottom = max_col_bottom[0] + i + 1
    
    max_row_left = np.where(df.iloc[i, 0:j] >= df.iloc[i, j])[0]
    if len(max_row_left) == 0:
        max_row_left = 0
    else:
        max_row_left = max_row_left[-1]
    
    max_row_right = np.where(df.iloc[i, j+1:] >= df.iloc[i, j])[0]
    if len(max_row_right) == 0:
        max_row_right = len(df.columns) - 1
    else:
        max_row_right = max_row_right[0] + j + 1

    score_left = j - max_row_left
    score_top = i - max_col_top
    score_right = max_row_right - j
    score_bottom = max_col_bottom - i


    # if df.iloc[i, j] > df.iloc[i, max_row_left]:
    #     score_left = j
    # else:
    #     score_left = j - max_row_left
    # if df.iloc[i, j] > df.iloc[max_col_top, j]:
    #     score_top = i
    # else:
    #     score_top = i - max_col_top
    # if df.iloc[i, j] > df.iloc[i, max_row_right]:
    #     score_right = len(df.columns) - j - 1
    # else:
    #     score_right = max_row_right - j
    # if df.iloc[i, j] > df.iloc[max_col_bottom, j]:
    #     score_bottom = len(df.index) - 1 - i
    # else:
    #     score_bottom = max_col_bottom - i
    return score_left * score_top * score_right * score_bottom


# count = 392
scores = []
for i in range(1, len(df.index) - 1):
    for j in range(1, len(df.columns) - 1):
        # if is_visible(i, j):
        #     count += 1
        # print(i, j, scenic_score(i, j))
        scores.append(scenic_score(i, j))

print(np.max(scores))


