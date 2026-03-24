from turtle import Turtle


MOVE_DISTANCE = 20


class Paddle(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.goto(position)
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        paddle_newy = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), paddle_newy)

    def down(self):
        paddle_newy = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), paddle_newy)

