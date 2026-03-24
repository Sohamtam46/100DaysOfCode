from turtle import Turtle, Screen
import random

# jim = Turtle()
screen = Screen()

# Sketch using the turtle
#
# def move_forward():
#     jim.forward(50)
#
# def move_left():
#     jim.setheading(jim.heading() + 5)
#
# def move_right():
#     jim.setheading(jim.heading() - 5)
#
# def move_backward():
#     jim.backward(50)
#
# def clear_screen():
#     turtle.resetscreen()
#
#
# screen.onkey(fun = move_forward,key = "Up")
# screen.onkeypress(fun = move_backward,key = "Down")
# screen.onkeypress(fun = move_left,key = "Left")
# screen.onkey(fun = move_right,key = "Right")
# screen.onkey(fun= clear_screen, key = "c")
# screen.listen()


# Turtle Racing Game
screen.setup(width=500, height=400)

user_bet_color = screen.textinput(title="Make your bet", prompt="Which Turtle would win the race? (enter color)")
colors = ["red", "orange", "blue", "green", "yellow", "violet"]

turtles = []

y = -150

for racer_index in range (0,6):
    racer = Turtle(shape="turtle")
    racer.color(colors[racer_index])
    turtles.append(racer)
    racer.penup()
    racer.goto(-230, y)
    y += 50

fastest_racer_position = -200
while fastest_racer_position <=  220:
    for racer in turtles:
        racer.fd(random.randint(0,10))
        racer_position_x = int(racer.xcor())
        if racer_position_x > fastest_racer_position:
            fastest_racer_position = racer_position_x
            fastest_racer_color = racer.color()[0]

if user_bet_color == fastest_racer_color:
    print("You win!")
else:
    print(f"You lose!, fastest turtle was {fastest_racer_color}")


screen.exitonclick()
