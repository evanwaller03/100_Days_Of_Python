import math

def paint_calc(width, height):
    area = width * height
    return math.ceil(area/5)

width = int(input("Wall Width: "))
height = int(input("Wall Height: "))
cans_needed = paint_calc(width = width, height = height)

print(f"You need {cans_needed} cans of paint.")


