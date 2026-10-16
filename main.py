import numpy as np
import random
import subprocess
import time

def render_matrix(matrix):
    """
    Prints the matrix onto the terminal.
    """
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] == 1:
                # This function specifically only renders the live (1s) cells.
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

def clear_screen():
    """Instructs the terminal to clear the screen."""
    # print("\x1b[2J\x1b[H", end = "", flush = True)
    subprocess.run("cls", shell = True)
    print("\x1b[?25l")

rows = 20
columns = 100
matrix = np.full((rows, columns), 0)

iteration = 0

while(True):
    clear_screen()

    if iteration == 0:
        seed = round(0.50 * (rows * columns))
        for i in range(seed):
            x = random.randint(1, rows - 2)
            y = random.randint(1, columns - 2)
            matrix[x][y] = 1
        render_matrix(matrix)

    else:
        new_matrix = np.copy(matrix)

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

                # Updated new matrix for the next iteration/generation with the rules applied.
                if matrix[x][y] == 1:
                    if counter < 2: new_matrix[x][y] = 0
                    elif counter == 2 or counter == 3: new_matrix[x][y] = 1
                    elif counter > 3: new_matrix[x][y] = 0

                elif matrix[x][y] == 0:
                    if counter == 3: new_matrix[x][y] = 1

        render_matrix(new_matrix)
        matrix = new_matrix

    iteration += 1
    time.sleep(0.2)