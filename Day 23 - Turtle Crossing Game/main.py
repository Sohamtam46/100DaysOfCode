import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")

player = Player()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.ycor() >= 300:
        player.position_reset()
        scoreboard.level_increase()


screen.exitonclick()