# to extract colors from a picture
# import colorgram
#
#
# colors = colorgram.extract('pic.jpg',30)
#
# color_list = []
# for color in colors:
#     individual_color = (color.rgb.r,color.rgb.g,color.rgb.b)
#     color_list.append(individual_color)
# print(color_list)

import turtle as t
import random

jim = t.Turtle()
t.colormode(255)
jim.speed("fastest")

jim.penup()
jim.setheading(225)
jim.forward(300)
jim.setheading(0)
initial_pos = jim.pos()

color_list = [(207, 156, 102), (231, 215, 96), (161, 55, 91), (42, 110, 152), (199, 138, 160), (123, 171, 194), (206, 73, 108), (140, 84, 67), (31, 167, 203), (205, 91, 76), (47, 122, 96), (33, 45, 66), (225, 170, 191), (126, 38, 68), (131, 181, 166), (45, 53, 106), (57, 38, 47), (147, 211, 221), (158, 157, 69), (161, 209, 195), (77, 160, 128), (19, 92, 76), (226, 176, 168), (54, 43, 40), (24, 59, 53), (109, 120, 161)]

for _ in range (10):
    for _ in range (10):
        jim.pendown()
        jim.dot(20,random.choice(color_list))
        jim.penup()
        jim.forward(50)
    current_pos = jim.pos()
    jim.setx(initial_pos[0])
    jim.sety(current_pos[1] + 40)


screen = t.Screen()
screen.exitonclick()
