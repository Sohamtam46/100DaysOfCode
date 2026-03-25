import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crossing")
screen.register_shape("car","car.gif")

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.listen()
screen.onkey(player.up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    # create and move the cars
    car_manager.create_cars()
    car_manager.car_move()

    # detect player reaching finish line and level up
    if player.ycor() >= 300:
        player.position_reset()
        scoreboard.level_increase()
        car_manager.level_increase()

    # detect collision of player with car
    for car in car_manager.cars:
        if player.distance(car) < 30:
            game_is_on = False
            car_manager.game_over()
            scoreboard.game_over()

screen.exitonclick()