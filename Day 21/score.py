from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_one_score = 0
        self.player_two_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, (600/2)-100)
        self.refresh()
        
    
    def p_one_point(self):
        self.player_one_score += 1
        self.refresh()
    
    def p_two_point(self):
        self.player_two_score += 1
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"{self.player_one_score} | {self.player_two_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)


    
