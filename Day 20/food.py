from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5,.5)
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)
        self.color('red')
        self.speed('fastest')