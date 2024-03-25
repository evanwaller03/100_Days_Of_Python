import pygame
from numpy import array
from math import cos, sin

######################
#    Math Section    #
######################

X, Y, Z = 0, 1, 2

def rotation_matrix(α, β, γ):
    sα, cα = sin(α), cos(α)
    sβ, cβ = sin(β), cos(β)
    sγ, cγ = sin(γ), cos(γ)
    return (
        (cβ*cγ, -cβ*sγ, sβ),
        (cα*sγ + sα*sβ*cγ, cα*cγ - sγ*sα*sβ, -cβ*sα),
        (sγ*sα - cα*sβ*cγ, cα*sγ*sβ + sα*cγ, cα*cβ)
    )

class Physical:
    def __init__(self, vertices, edges):
        self.__vertices = array(vertices)
        self.__edges = tuple(edges)
        self.__rotation = [0, 0, 0]

    def rotate(self, axis, θ):
        self.__rotation[axis] += θ

    def get_faces(self):
        # Define each face by the indices of its vertices
        return [
            [self.__vertices[i] for i in [0, 1, 4, 5]],  # Top face
            [self.__vertices[i] for i in [2, 3, 6, 7]],  # Bottom face
            [self.__vertices[i] for i in [0, 1, 2, 3]],  # Front face
            [self.__vertices[i] for i in [4, 5, 6, 7]],  # Back face
            [self.__vertices[i] for i in [0, 2, 4, 6]],  # Left face
            [self.__vertices[i] for i in [1, 3, 5, 7]],  # Right face
        ]

    @property
    def lines(self):
        location = self.__vertices.dot(rotation_matrix(*self.__rotation))
        return ((location[v1], location[v2]) for v1, v2 in self.__edges)

######################
#     GUI Section    #
######################

BLACK, RED = (0, 0, 0), (255, 128, 128)

class Paint:
    def __init__(self, shapes, keys_handler):
        self.__shapes = shapes
        self.__keys_handler = keys_handler
        self.__size = 1000, 1000
        self.__screen = pygame.display.set_mode(self.__size)
        self.__clock = pygame.time.Clock()
        self.__scale = 35  # Adjust as needed for visual preference
        pygame.init()
        self.__mainloop()

    def __fit(self, vec):
        # Adjusted centering logic to account for new scale
        center_screen = array(self.__size) / 2
        return [round(self.__scale * coordinate + center) for coordinate, center in zip(vec, center_screen)]


    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        self.__keys_handler(pygame.key.get_pressed())

    def __draw_shapes(self):
        GREY = (192, 192, 192)  # Grey color for filling the faces

        for shape in self.__shapes:
            faces = shape.get_faces()  # Get the faces of the cube
            for face in faces:
                # Transform face vertices to screen coordinates
                polygon_points = [self.__fit(vertex) for vertex in face]
                # Draw filled polygon for each face
                pygame.draw.polygon(self.__screen, GREY, polygon_points)

    def __draw_shapes(self, thickness=1):
        GREY = (192, 192, 192)  # Define grey color for the cube edges

        for shape in self.__shapes:
            # Draw the edges in grey to simulate a solid appearance
            for start, end in shape.lines:
                pygame.draw.line(self.__screen, GREY, self.__fit(start), self.__fit(end), thickness)



    def __mainloop(self):
        while True:
            self.__handle_events()
            self.__screen.fill(BLACK)
            self.__draw_shapes()
            pygame.display.flip()
            self.__clock.tick(40)

######################
#     Main Start     #
######################

def create_cubes(n=5, offset=1.5):
    base_vertices = tuple((x/4, y/4, z/4) for x, y, z in [
        (1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1),
        (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)
    ])
    edges = (
        {0, 1}, {0, 2}, {2, 3}, {1, 3},
        {4, 5}, {4, 6}, {6, 7}, {5, 7},
        {0, 4}, {1, 5}, {2, 6}, {3, 7}
    )

    # Center the cube array at the origin
    center_offset = -(n-1)/2 * offset
    cubes = []
    for x in range(n):
        for y in range(1):
            for z in range(n):
                vertices = tuple((vx+(x*offset+center_offset), vy+(y*offset+center_offset), vz+(z*offset+center_offset)) for vx, vy, vz in base_vertices)
                cubes.append(Physical(vertices, edges))
    return cubes

def main():
    from pygame import K_q, K_w, K_a, K_s, K_z, K_x

    # Parameters for cube rotations, might not be needed if we lock orientation
    # counter_clockwise = 0.05
    # clockwise = -counter_clockwise
    params = {
        # Remove or comment out rotation parameters if you want to lock the orientation
    }

    def keys_handler(keys):
        pass  # Empty handler to prevent rotations

    # Adjust the create_cubes call for a 25x25 grid and smaller cubes
    cubes = create_cubes(n=15, offset=0.5)  # Adjust 'offset' for cube spacing, n=25 for a 25x25 grid

    # Set an initial orientation for a 3D appearance
    initial_rotation_x = -0.4  # Adjust these angles for the desired 3D effect
    initial_rotation_y = 0.3
    for cube in cubes:
        cube.rotate(X, initial_rotation_x)
        cube.rotate(Y, initial_rotation_y)

    pygame.display.set_caption('25x25 Cube Grid - Static 3D View')
    Paint(cubes, keys_handler)

if __name__ == '__main__':
    main()