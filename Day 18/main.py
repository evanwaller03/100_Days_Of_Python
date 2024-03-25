import turtle as t
from random import randint

tom = t.Turtle()
t.colormode(255)

side_length = 100

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)
    return rand_color

def drawShape(sides, length):
    
    tom.pencolor(random_color())

    total_degrees = 180 + 180*(sides-3)
    print(total_degrees)
    turning_degrees = 180 - total_degrees/sides
    print(turning_degrees)
    for num in range(1,sides):
        tom.forward(length)
        tom.right(turning_degrees)
    
        

for number_of_sides in range(3, 11):
    drawShape(number_of_sides, side_length)

drawShape(3, side_length)

t.done()
