from turtle import Turtle,Screen

screen = Screen()
# NEW_SQUARE = Turtle(shape="square")

# three positions for the first three squares
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class Snake:

    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        # the following block creates the body of the snakes
        # creating three squares which start at three diff position(20 difference cause of the size of each square)
        for position in STARTING_POSITION:
            self.add_square(position)

    def snake_size_increase(self):
        position = (self.squares[-1].position())
        self.add_square(position)

    def add_square(self,position):
        new_square = Turtle(shape="square")
        new_square.penup()
        new_square.goto(position)
        new_square.color("white")
        self.squares.append(new_square)

    def move(self):
        """Following Method will move the snake"""
        # the following for loop will ensure all the squares move as one body
        # we take the last square and move it to second last squares position
        # and do the same for all the squares leading upto the second square.
        for square_num in range(len(self.squares)-1,0,-1):
            new_x = self.squares[square_num - 1].xcor()
            new_y = self.squares[square_num - 1].ycor()
            self.squares[square_num].goto(new_x,new_y)
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

