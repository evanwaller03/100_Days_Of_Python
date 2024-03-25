from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
import time

# Adjusting grid size to 40x40
GRID_WIDTH = 20
GRID_HEIGHT = 20
MAX_HISTORY = 15

# Initialize grid with random states
grid = np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT))
grid_history = []

def setup_viewport():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)  # Enable lighting
    glEnable(GL_LIGHT0)  # Enable light #0
    glEnable(GL_LIGHT1)  # Enable an additional light source
    
    glLightfv(GL_LIGHT1, GL_POSITION, [-5.0, -5.0, 5.0, 1.0])  # Position of the second light
    glLightfv(GL_LIGHT1, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])  # Diffuse light
    glLightfv(GL_LIGHT1, GL_SPECULAR, [0.5, 0.5, 0.5, 1.0])  # Specular light
    # Define a simple light
    glLightfv(GL_LIGHT0, GL_POSITION, [5.0, 5.0, 5.0, 1.0])  # Position
    glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1.0])  # Ambient light
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.5, 0.5, 0.5, 1.0])  # Diffuse light

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, (800 / 600), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


def draw_cube(x, y, z, scale, color):
    glColor3fv(color)  # Set the color for fixed-function pipeline (for debugging)

    # Ensure color values are within [0, 1] range
    print("Color values:", color)  # Debugging: Check the actual color values

    # Change here: Convert [1.0] to (1.0,) to concatenate tuples
    cube_material_diffuse = color + (1.0,)  # Add alpha value
    cube_material_ambient = (color[0] * 0.5, color[1] * 0.5, color[2] * 0.5, 1.0)  # Dimmer ambient color

    glMaterialfv(GL_FRONT, GL_DIFFUSE, cube_material_diffuse)
    glMaterialfv(GL_FRONT, GL_AMBIENT, cube_material_ambient)

    glEnable(GL_LIGHTING)  # Ensure lighting is enabled for this object
    glBegin(GL_QUADS)
    
    # Remaining code in draw_cube function...

    
    # List of normals for each face
    normals = [
        [0, 0, 1], [0, 0, -1],  # Front, Back
        [-1, 0, 0], [1, 0, 0],  # Left, Right
        [0, 1, 0], [0, -1, 0]  # Top, Bottom
    ]

    # Vertex positions for the cube's faces
    vertices = [
        [[1, 1, 1], [-1, 1, 1], [-1, -1, 1], [1, -1, 1]],  # Front
        [[1, 1, -1], [1, -1, -1], [-1, -1, -1], [-1, 1, -1]],  # Back
        [[-1, 1, 1], [-1, 1, -1], [-1, -1, -1], [-1, -1, 1]],  # Left
        [[1, 1, -1], [1, 1, 1], [1, -1, 1], [1, -1, -1]],  # Right
        [[1, 1, -1], [-1, 1, -1], [-1, 1, 1], [1, 1, 1]],  # Top
        [[1, -1, 1], [-1, -1, 1], [-1, -1, -1], [1, -1, -1]]  # Bottom
    ]
    
    for i in range(6):
        glNormal3fv(normals[i])
        for vertex in vertices[i]:
            glVertex3f(x + vertex[0] * scale, y + vertex[1] * scale, z + vertex[2] * scale)
    
    glEnd()

def update_grid():
    global grid, grid_history
    new_grid = np.zeros((GRID_WIDTH, GRID_HEIGHT))
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            neighbors = np.sum(grid[max(x-1,0):min(x+2,GRID_WIDTH), max(y-1,0):min(y+2,GRID_HEIGHT)]) - grid[x, y]
            if grid[x, y] == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[x, y] = 1
            elif grid[x, y] == 0 and neighbors == 3:
                new_grid[x, y] = 1
    if len(grid_history) >= MAX_HISTORY:
        grid_history.pop(0)  # Remove the oldest snapshot
    grid_history.append(grid.copy())  # Add current snapshot to history
    grid = new_grid

def draw_grid():
    """Draw the grid based on the game of life states."""
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Define the camera position and view direction
    gluLookAt(0, -5, 10, 0, 0, 0, 0, 1, 0)

    
    # Draw grid history
    for i, snapshot in enumerate(grid_history):
        draw_snapshot(snapshot, i)
    
    glutSwapBuffers()
    glutPostRedisplay()

def draw_snapshot(snapshot, layer):
    camera_pos = (-1, -5, 7)  # This should be dynamically determined based on your camera setup
    layer_height = -layer * 0.2
    spacing = 0.25  # Additional spacing between cubes
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if snapshot[x, y] == 1:
                # Increase spacing by adjusting the multiplier and adding an explicit spacing term
                cube_x = (x - GRID_WIDTH / 2) * (0.2 + spacing)
                cube_y = (y - GRID_HEIGHT / 2) * (0.2 + spacing)

                cube_z = layer_height
                if is_cube_visible(cube_x, cube_y, cube_z, camera_pos):
                    distance = distance_to_center(x, y)
                    color = color_from_distance(distance)
                    glColor3f(*color)
                    color = color_from_distance(distance)
                    draw_cube(cube_x, cube_y, cube_z, 0.1, color)




def distance_to_center(x, y):
    """Calculate the distance from a cell to the center of the grid."""
    center_x, center_y = GRID_WIDTH // 2, GRID_HEIGHT // 2
    return np.sqrt((x - center_x)**2 + (y - center_y)**2)

def color_from_distance(distance):
    """Map distance to a color."""
    color_map = [
        (1.0, 0.0, 0.0),   # Red
        (1.0, 0.5, 0.0),   # Orange
        (1.0, 1.0, 0.0),   # Yellow
        (0.0, 1.0, 0.0),   # Green
        (0.0, 0.0, 1.0),   # Blue
        (0.5, 0.0, 0.5),   # Purple
        (1.0, 0.0, 1.0),   # Pink
        (1.0, 1.0, 1.0),   # White
        (0.5, 0.5, 0.5)    # Black
    ]
    max_distance = GRID_WIDTH // 2  # Maximum distance from the center
    index = min(int(distance / (max_distance / len(color_map))), len(color_map) - 1)
    return color_map[index]

def is_cube_visible(x, y, z, camera_pos, visibility_threshold=50):
    """
    Simplified visibility check based on distance from the camera.
    :param x: Cube's x position
    :param y: Cube's y position
    :param z: Cube's z position
    :param camera_pos: Tuple of the camera's (x, y, z) position
    :param visibility_threshold: How far from the camera a cube can be to be considered visible
    :return: True if the cube is likely visible, False otherwise
    """
    dx = x - camera_pos[0]
    dy = y - camera_pos[1]
    dz = z - camera_pos[2]
    distance_squared = dx * dx + dy * dy + dz * dz
    return distance_squared <= visibility_threshold ** 2

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
    glutInitWindowSize(1200, 1200)
    glutCreateWindow(b"Game of Life in 3D")

    glEnable(GL_DEPTH_TEST)
    setup_viewport()

    glutDisplayFunc(draw_grid)

    # Schedule the update_grid function to be called every 100 milliseconds
    glutTimerFunc(50, update_and_redraw, 0)

    glutMainLoop()  # Start the main loop

def update_and_redraw(value):
    update_grid()  # Update the game state
    glutPostRedisplay()  # Trigger a redraw
    global iterations
    iterations += 1
    if iterations >= 60:
        iterations = 0
        reset_grid()
    glutTimerFunc(100, update_and_redraw, 0)  # Schedule the next update

iterations = 0  # Global variable to track the number of iterations

def reset_grid():
    global grid
    grid = np.random.choice([0, 1], size=(GRID_WIDTH, GRID_HEIGHT))  # Reset the grid

# Other functions remain the same...

if __name__ == "__main__":
    main()

