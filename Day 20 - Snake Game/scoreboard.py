from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")



class Scoreboard(Turtle):


    def __init__(self):
        self.score = 0
        super().__init__()
        self.goto(x=0,y=270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)

    def score_increase(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
