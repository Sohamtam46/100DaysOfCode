from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.seth(90)
        self.color("black")
        self.penup()
        self.position_reset()

    def position_reset(self):
        self.goto(STARTING_POSITION)

    def up(self):
        self.fd(MOVE_DISTANCE)
