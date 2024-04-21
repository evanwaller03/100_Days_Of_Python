from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from score import Score

# Screen Initialization
WIDTH = 800 # Global
HEIGHT = 600 # Global
screen = Screen() # Screen Initialization
screen.setup(width=WIDTH,height=HEIGHT) # Set height and width of screen
screen.bgcolor('black') # Set BG color
screen.title("Pong") # Set title
screen.tracer(0)

player_one = Paddle(((-WIDTH/2)+50, 0))
player_two = Paddle(((WIDTH/2)-50, 0))
ball = Ball()
scoreboard = Score()

screen.listen()
screen.onkey(player_one.move_up, "w")
screen.onkey(player_one.move_down, "s")
screen.onkey(player_two.move_up, "Up")
screen.onkey(player_two.move_down, "Down")

def run_game():
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.speed)
        ball.move()

        if ball.ycor() > (HEIGHT/2)-20 or ball.ycor() < (-HEIGHT/2)+20: 
            ball.y_bounce()
        
        if ball.distance(player_one) < 50 and ball.xcor() < (-WIDTH/2)+80 or ball.distance(player_two) < 50 and ball.xcor() > (WIDTH/2)-80 : 
            ball.x_bounce()

        if ball.xcor() < -WIDTH/2 + 20: 
            scoreboard.p_two_point()
            ball.reset()
        
        if ball.xcor() > WIDTH/2 - 20:
            scoreboard.p_one_point()
            ball.reset()
        
        if scoreboard.player_one_score == 3 or scoreboard.player_two_score == 3:
            scoreboard.game_over()
            game_is_on = False

run_game()

screen.exitonclick()