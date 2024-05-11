import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Constants for a 50x50 grid
CELL_SIZE = 10  # Pixel size of each cell
GRID_WIDTH, GRID_HEIGHT = 50, 50  # Grid dimensions
WIDTH, HEIGHT = CELL_SIZE * GRID_WIDTH, CELL_SIZE * GRID_HEIGHT  # Screen dimensions

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH*2, HEIGHT*2))
pygame.display.set_caption("Conway's Game of Life")

def draw_3d_grid(screen, grid):
    offset_x, offset_y = WIDTH // 4, HEIGHT // 10  # Adjust as needed for visual offset
    cell_width, cell_height = CELL_SIZE, CELL_SIZE // 2  # Adjust cell_height for 3D effect
    depth = CELL_SIZE // 4  # Adjust for depth effect

    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = BLACK if grid[row][col] == 1 else WHITE
            # Calculate the base points for the parallelogram/trapezoid
            base_x = col * cell_width + offset_x - row * depth + WIDTH * 0.5  # Adjusted for midpoint
            base_y = row * cell_height + offset_y + col * depth + HEIGHT * 0.25  # Adjusted for midpoint

            # Define the points for the parallelogram/trapezoid
            points = [
                (base_x, base_y),  # Top left
                (base_x + cell_width, base_y + depth),  # Top right
                (base_x + cell_width - depth, base_y + cell_height + depth),  # Bottom right
                (base_x - depth, base_y + cell_height)  # Bottom left
            ]

            pygame.draw.polygon(screen, color, points)

def update_grid(grid):
    new_grid = grid.copy()
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            # Count live neighbors, considering wrap-around at edges
            live_neighbors = np.sum(grid[row-1 if row-1 >= 0 else GRID_HEIGHT-1:row+2 if row+2 < GRID_HEIGHT else 1, col-1 if col-1 >= 0 else GRID_WIDTH-1:col+2 if col+2 < GRID_WIDTH else 1]) - grid[row, col]
            # Apply the rules
            if grid[row, col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[row, col] = 0
            elif grid[row, col] == 0 and live_neighbors == 3:
                new_grid[row, col] = 1
    return new_grid

def main():
    running = True
    grid = np.random.choice([0, 1], GRID_WIDTH*GRID_HEIGHT, p=[0.8, 0.2]).reshape(GRID_HEIGHT, GRID_WIDTH)
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill(WHITE)
        draw_3d_grid(screen, grid)  # Updated to draw a 3D grid
        pygame.display.flip()
        grid = update_grid(grid)
        pygame.time.wait(100)  # Wait a bit for the next generation

    pygame.quit()

if __name__ == "__main__":
    main()
