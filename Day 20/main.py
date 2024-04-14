# Day 1:
    # Create a snake body
    # Move the snake
    # Control the snake


# Day 2:
    # Detect collision with food
    # Keep track of score (create score board)
    # Detect collision with wall
    # Detect collision with tail

from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from score import Score

# Screen Initialization
WIDTH = 600 # Global
HEIGHT = 600 # Global
screen = Screen() # Screen Initialization
screen.setup(width=WIDTH,height=HEIGHT) # Set height and width of screen
screen.bgcolor('black') # Set BG color
screen.title("Classic Snake Game") # Set title
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.add_segment, "C")
screen.onkey(snake.counter, "P")

game_is_on = True
while game_is_on: 
    screen.update()
    time.sleep(.1)

    snake.move()
 
    #Detect collision with food
    if snake.head.distance(food) < 15:
        print("Nom nom nom")

screen.exitonclick()
