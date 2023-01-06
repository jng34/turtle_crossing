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
car = Car()

screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()
    if player.ycor() == -100:
        scoreboard.add_score()
        player.restart()
