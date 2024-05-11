import pygame
from numpy import array
from math import cos, sin


######################
#                    #
#    math section    #
#                    #
######################

X, Y, Z = 0, 1, 2


def rotation_matrix(α, β, γ):
    """
    rotation matrix of α, β, γ radians around x, y, z axes (respectively)
    """
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
        """
        a 3D object that can rotate around the three axes
        :param vertices: a tuple of points (each has 3 coordinates)
        :param edges: a tuple of pairs (each pair is a set containing 2 vertices' indexes)
        """
        self.__vertices = array(vertices)
        self.__edges = tuple(edges)
        self.__rotation = [0, 0, 0]  # radians around each axis

    def rotate(self, axis, θ):
        self.__rotation[axis] += θ

    @property
    def lines(self):
        location = self.__vertices.dot(rotation_matrix(*self.__rotation))  # an index->location mapping
        return ((location[v1], location[v2]) for v1, v2 in self.__edges)


######################
#                    #
#    gui section     #
#                    #
######################


BLACK, RED = (0, 0, 0), (255, 128, 128)


class Paint:
    def __init__(self, shape, keys_handler):
        self.__shape = shape
        self.__keys_handler = keys_handler
        self.__size = 450, 450
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(self.__size)
        self.__mainloop()

    def __fit(self, vec):
        """
        ignore the z-element (creating a very cheap projection), and scale x, y to the coordinates of the screen
        """
        # notice that len(self.__size) is 2, hence zip(vec, self.__size) ignores the vector's last coordinate
        return [round(70 * coordinate + frame / 2) for coordinate, frame in zip(vec, self.__size)]

    def __handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        self.__keys_handler(pygame.key.get_pressed())

    def __draw_shape(self, thickness=4):
        for start, end in self.__shape.lines:
            pygame.draw.line(self.__screen, RED, self.__fit(start), self.__fit(end), thickness)

    def __mainloop(self):
        while True:
            self.__handle_events()
            self.__screen.fill(BLACK)
            self.__draw_shape()
            pygame.display.flip()
            self.__clock.tick(40)
def main():
    from pygame import K_q, K_w, K_a, K_s, K_z, K_x

    # Adjust the vertices to represent a 3x3 flat grid (z is constant, indicating a single layer)
    vertices = (
        (-1, 1, 0),  # Top left corner
        (0, 1, 0),   # Top middle
        (1, 1, 0),   # Top right corner
        (-1, 0, 0),  # Middle left
        (0, 0, 0),   # Center
        (1, 0, 0),   # Middle right
        (-1, -1, 0), # Bottom left corner
        (0, -1, 0),  # Bottom middle
        (1, -1, 0)   # Bottom right corner
    )

    # Define edges for a 3x3 grid (both perimeter and internal lines)
    edges = (
        {0, 1}, {1, 2}, # Top horizontal lines
        {3, 4}, {4, 5}, # Middle horizontal lines
        {6, 7}, {7, 8}, # Bottom horizontal lines
        {0, 3}, {3, 6}, # Left vertical lines
        {1, 4}, {4, 7}, # Middle vertical lines
        {2, 5}, {5, 8}  # Right vertical lines
    )

    cube = Physical(vertices=vertices, edges=edges)

    counter_clockwise = 0.05  # radians
    clockwise = -counter_clockwise

    params = {
        K_q: (X, clockwise),
        K_w: (X, counter_clockwise),
        K_a: (Y, clockwise),
        K_s: (Y, counter_clockwise),
        K_z: (Z, clockwise),
        K_x: (Z, counter_clockwise),
    }

    def keys_handler(keys):
        for key in params:
            if keys[key]:
                cube.rotate(*params[key])

    pygame.init()
    pygame.display.set_caption('3x3x1 Grid -   q,w : X    a,s : Y    z,x : Z')
    Paint(cube, keys_handler)

if __name__ == '__main__':
    main()
