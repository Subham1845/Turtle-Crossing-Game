import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forward, "Up")

game_is_on = True
while game_is_on:
    time.sleep(scoreboard.move_speed)
    screen.update()
    car_manager.create_cars()
    car_manager.car_move()

    # Game Over
    for car in car_manager.turtles:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    # Level update
    if player.ycor() > 280:
        scoreboard.update_level()
        player.reset()

screen.exitonclick()