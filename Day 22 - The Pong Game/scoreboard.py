from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):


    def __init__(self,x_position):
        super().__init__()
        self.score = 0
        self.goto(x=x_position,y=240)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"{self.score}", align= ALIGNMENT, font=FONT)

    def score_increase(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()