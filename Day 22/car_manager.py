from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
LEVELED_UP = 5


class CarManager():
    
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(180)
            new_car.color(COLORS[random.randint(0, len(COLORS)-1)])
            new_car.shapesize(1,2)
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            new_x = car.xcor() - self.car_speed
            car.goto(new_x, car.ycor())

    
    def level_up(self):
        self.car_speed += LEVELED_UP


    def delete_car(self, car):
        car.hideturtle()
        car.clear()
        if car in self.all_cars:
            self.all_cars.remove(car)