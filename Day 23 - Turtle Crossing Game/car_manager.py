from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        if random.randint(1,6) == 1:
            new_car = Turtle(shape="square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.seth(180)
            new_car.goto(280,random.randint(-200,200))
            self.cars.append(new_car)
            new_car.shapesize(stretch_wid=1, stretch_len=2)


    def level_increase(self):
        self.car_speed += MOVE_INCREMENT


    def car_move(self):
        cars_copy = self.cars[:]
        for car in cars_copy:
            car.fd(self.car_speed)


    def game_over(self):
        self.car_speed = 0
