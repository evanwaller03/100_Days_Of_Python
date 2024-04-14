from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)
    
    def create_snake(self):
        for position in STARTING_POSITIONS:
            snake_segment = Turtle(shape="square")
            snake_segment.color('white')
            snake_segment.penup()
            snake_segment.speed("slowest")
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def add_segment(self):
        snake_segment = Turtle(shape="square")
        snake_segment.color('white')
        snake_segment.penup()
        snake_segment.speed("slowest")
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        snake_segment.goto(new_x, new_y)
        self.segments.append(snake_segment)
    
    def counter(self):
        print(len(self.segments))

    
    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)


    

