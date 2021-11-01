import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
scoreboard.writetext()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
game_is_on = True
screen.listen()
all_cart = []
# for num in range(5):
#     car_manager = CarManager()
#     all_cart.append(car_manager)
num1 = 1
while game_is_on:
    num1 += 1
    screen.onkey(player.movet, "Up")
    if num1 == 6:
        num1 = 1
        car_manager = CarManager()
        all_cart.append(car_manager)

    for car in all_cart:
        car.move_car()
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        if car.ycor() < -280:
            car.clear()
            all_cart.remove(car)
    if player.ycor() > 280:
        player.won()
        scoreboard.score += 1
        scoreboard.writetext()

    screen.update()
    time.sleep(0.1)

screen.exitonclick()
