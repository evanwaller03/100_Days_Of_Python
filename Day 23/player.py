from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.color("black")
        self.goto(STARTING_POSITION)
    
    def move_up(self):
        if self.ycor() <= 280:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(0, new_y)

    def move_down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(0, new_y)
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False