from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.food_eaten = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, (600/2)-(600/20))
        self.refresh()
        
    
    def add(self):
        self.food_eaten += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score = {self.food_eaten}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)


    
