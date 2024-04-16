from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        
    def create_cars(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.setheading(180)
        new_car.color(COLORS[random.randint(0, len(COLORS)-1)])
        new_car.shapesize(1,2)
        new_car.goto(300, random.randint(-270, 270))
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - MOVE_INCREMENT
            car.goto(new_x, car.ycor())

    def delete_car(self, car):
        car.hideturtle()
        car.clear()
        if car in self.all_cars:
            self.all_cars.remove(car)
