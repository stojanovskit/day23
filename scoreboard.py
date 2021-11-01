from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

    def writetext(self):
        self.clear()
        self.write(f"Score: {self.score}", FONT)
        self.goto(0, 280)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", FONT)


