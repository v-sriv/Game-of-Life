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