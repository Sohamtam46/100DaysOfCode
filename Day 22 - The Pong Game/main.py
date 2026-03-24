from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
l_score = Scoreboard(-60)
r_score = Scoreboard(60)

screen.listen()
# why up with the brackets??
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on = True
ball_top_hit = False



while game_is_on:

    screen.update()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_top_bottom()


    if  (ball.xcor() >= 330 or ball.xcor() <= -330) and (r_paddle.distance(ball) <= 50 or l_paddle.distance(ball) <= 50):
        ball.bounce_right_left()


    if ball.xcor() > 350:
        ball.reset_position()
        l_score.score_increase()


    if ball.xcor() <= -350:
        ball.reset_position()
        r_score.score_increase()


    ball.move()
    time.sleep(ball.move_speed)



screen.exitonclick()

