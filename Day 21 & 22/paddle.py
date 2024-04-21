from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()   
        self.goto(position)
        self.y_move = 10
        
    def move_up(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - self.y_move
        self.goto(self.xcor(), new_y)