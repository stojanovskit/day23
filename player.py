from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def movet(self):
        new_y = self.ycor() + MOVE_DISTANCE
        new_x = self.xcor()
        self.goto(new_x, new_y)

    def won(self):
        self.goto(STARTING_POSITION)



