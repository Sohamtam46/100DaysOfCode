from turtle import Screen
from Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")     
screen.title("Snake Game")
# animation off so the screen only updates when we want it to
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_on = True

while game_on:

    screen.update()
    # to slow down the snake
    time.sleep(0.4)
    snake.move()

    # collision detection with food
    if snake.head.distance(food) < 15:
        # place the food in a random place
        food.refresh()
        # update the score by 1
        scoreboard.score_increase()
        snake.snake_size_increase()

    # collision detection with wall
    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        scoreboard.game_over()
        game_on = False


    # collision detection with tail
    for square in snake.squares[1:]:
        if snake.head.distance(square) < 10:
            game_on = False
            scoreboard.game_over()







screen.exitonclick()