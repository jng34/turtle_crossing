import time
from turtle import Screen
from player import Player
from car import Car
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_generator = Car()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_generator.create_car()
    car_generator.move_car(scoreboard.level)

    # Detect player at finish line
    if player.at_finish_line():
        scoreboard.add_score()
        player.restart()

    # Detect player collision with car
    for car in car_generator.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()