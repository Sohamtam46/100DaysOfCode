from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):


    def __init__(self):
        self.score = 0
        with open("./highscore data/highscore.txt") as data:
            self.highscore = int(data.read())
        super().__init__()
        self.goto(x=0,y=270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def game_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("./highscore data/highscore.txt",mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score = {self.highscore}", align= ALIGNMENT, font=FONT)

    def score_increase(self):
        self.score += 1
        self.update_scoreboard()
