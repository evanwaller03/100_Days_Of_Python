import numpy as np
import time
import os

def create_grid(size):
    return np.random.choice([0, 1], size*size, p=[0.8, 0.2]).reshape(size, size)

def apply_rules(grid):
    new_grid = grid.copy()
    for r in range(grid.shape[0]):
        for c in range(grid.shape[1]):
            # Count live neighbors
            live_neighbors = np.sum(grid[r-1:r+2, c-1:c+2]) - grid[r, c]
            # Apply the rules
            if grid[r, c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[r, c] = 0
            elif grid[r, c] == 0 and live_neighbors == 3:
                new_grid[r, c] = 1
    return new_grid

def display_grid(grid):
    os.system('cls' if os.name == 'nt' else 'clear')
    for row in grid:
        print(' '.join(['⬜️' if cell == 0 else '⬛️' for cell in row]))
    time.sleep(0.1)

def main():
    size = 60 # Size of the grid
    grid = create_grid(size)
    generations = 200  # Number of generations
    for _ in range(generations):
        display_grid(grid)
        grid = apply_rules(grid)

if __name__ == "__main__":
    main()
