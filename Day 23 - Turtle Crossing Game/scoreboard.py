from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(x=-200,y=250)
        self.update_level()
        self.hideturtle()

    def update_level(self):
        self.write(f"Level = {self.level}", align= ALIGNMENT, font=FONT)

    def level_increase(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align= ALIGNMENT, font=FONT)
