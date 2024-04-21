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
score = Score()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def run_game():
    game_is_on = True
    while game_is_on: 
        screen.update()
        time.sleep(.1)

        snake.move()
        
        #Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            score.add()
            snake.extend()

        if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            score.reset()
            snake.reset()
        
        for seg in snake.segments[1:]:
            if snake.head.distance(seg) < 10:
                score.reset()
                snake.reset()

run_game()  

screen.exitonclick()
