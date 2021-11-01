from turtle import Turtle
from scoreboard import Scoreboard
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=random.randint(2, 4))
        self.setheading(180)
        self.goto(280, random.randint(-250, 250))

    def move_car(self):
        self.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * Scoreboard().score))
