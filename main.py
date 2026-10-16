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


# The range goes from 1 to "rows" - 1 (and not 0 to rows) because the edge indices will return an out-of-bound value when neighbors() is called.
for x in range(1, rows - 1):
    for y in range(1, columns - 1):

        counter = 0
        neighboring_indices = neighbors(x, y)

        # Population counter based on "live/1" or "dead/0" cells
        for i in neighboring_indices:
            if matrix[i[0]][i[1]] == 1:
                counter += 1
            else: continue