from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.food_eaten = 0
        with open("/Users/evanwaller/Desktop/GitHub Projects/100 Days of Code/Day 24/highscore.txt") as f:
                contents = f.read()
                self.high_score = int(contents)
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
        self.write(f"Score: {self.food_eaten}  Highscore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.food_eaten > self.high_score:
            self.high_score = self.food_eaten
            with open("/Users/evanwaller/Desktop/GitHub Projects/100 Days of Code/Day 24/highscore.txt", mode='w') as f:
                f.write(f"{self.high_score}")
        self.food_eaten = 0
        self.refresh()


    
