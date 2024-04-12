from turtle import Turtle, Screen
import random

screen = Screen()
colors = [ "red", "orange", "yellow", "green", "blue", "purple", "pink"]
WIDTH = 500
HEIGHT = 500
screen.setup(WIDTH,HEIGHT)

def starting_line(colors):
    new_turtles = []
    for color in colors:
        add_turtle = Turtle(shape="turtle")
        add_turtle.speed(0)
        add_turtle.penup()
        add_turtle.color(color)
        new_turtles.append(add_turtle)

    buffer = 50
    count = 0
    for turtle in new_turtles:
        turtle.goto((WIDTH/2)*(-1)+20, 0-(len(new_turtles)/2*buffer)+(buffer*count))
        count += 1
    return new_turtles

def race(turtles):
    while True:
        for turtle in turtles:
            step = random.randint(3,10)
            turtle.forward(step)
            if turtle.xcor() >= WIDTH/2:
                return turtle
                
turtles = starting_line(colors)

user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")

winner = race(turtles)

if winner.color()[0] == user_bet:
    print(f"Congrats! You chose the {winner.color()[0]} turtle and it won!")
else:
    print(f"The winner is the {winner.color()[0]} turtle!")

screen.exitonclick()