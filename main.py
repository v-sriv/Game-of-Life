import numpy as np

rows = 10
columns = 100
matrix = np.full((rows, columns), 0)

for i in range(rows):
    for j in range(columns):
        if matrix[i][j] == 0:
            print("*", end = " ")
        else:
            print(" ", end = " ")
    print(f"\n", end = " ")