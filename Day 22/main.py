import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def run_game():

    
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)

    car_manager = CarManager()
    player = Player()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(player.move_up, "Up")
    screen.onkey(player.move_down, "Down")

    game_is_on = True

    while game_is_on:
        time.sleep(0.1)
        screen.update()

        car_manager.create_cars()
        car_manager.move()
        for car in car_manager.all_cars:
            if player.distance(car) < 20:
                game_is_on = False
                scoreboard.game_over()
                
            if car.xcor() < -300:
                car_manager.delete_car(car)
            
        if player.at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.inc_score()

    screen.exitonclick()

def play_another(screen):
    screen.clear()
    run_game()

run_game()

