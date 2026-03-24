from turtle import Turtle, Screen
import turtle as t
import random

jim = Turtle()
jim.shape("turtle")
jim.color("blue")

# # draw square
# for _ in range (4):
#     jim.forward(100)
#     jim.right(90)

# # draw dotted lines
# for _ in range (50):
#     jim.down()
#     jim.forward(5)
#     jim.penup()
#     jim.forward(5)


# # draw multiple shapes in random color
# i = 3
#
# for _ in range (7):
#     jim.color(random.random(),random.random(),random.random())
#     for _ in range (i):
#         jim.forward(100)
#         jim.right(360 / i)
#     i += 1


# # random walk within set boundaries
# angle = [0,90,180, 270]
# jim.pensize(10)
# jim.speed("fastest")
# for _ in range (100):
#     if (-90<jim.xcor()<90) and (-90<jim.ycor()<90):
#         jim.setheading(random.choice(angle))
#         jim.forward(30)
#     else:
#         jim.right(180)
#         jim.forward(30)
#     jim.color(random.random(), random.random(), random.random())


# random color with colormode
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     my_t = (r,g,b)
#     return my_t
#
# for _ in range (10):
#     jim.forward(50)
#     jim.right(90)
#     jim.color(random_color())

# Draw a spirograph

# t.colormode(255)
# jim.speed("fastest")
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r,g,b)
#     return color
#
# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         jim.circle(100)
#         jim.setheading(jim.heading() + size_of_gap)
#         jim.color(random_color())
#
# draw_spirograph(5)

screen = Screen()
screen.exitonclick()
