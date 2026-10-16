import numpy as np
import random

rows = 10
columns = 100
matrix = np.full((rows, columns), 0)


for i in range(rows):
    for j in range(columns):
        matrix[i][j] = random.randint(0, 1)
        if matrix[i][j] == 1:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print(f"\n", end = " ")

def neighbors(x, y):
    """
    Returns the coordinates of all eight cells in the Moore neighborhood surrounding the cell at position (x, y).
    """
    neighbors = [[x - 1, y - 1], [x - 1, y], [x - 1, y + 1], 
                 [x, y - 1], [x, y + 1],
                 [x + 1, y - 1], [x + 1, y], [x + 1, y + 1]]
    return neighbors