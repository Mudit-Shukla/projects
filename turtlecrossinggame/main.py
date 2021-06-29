import time
from turtle import Screen
from turtlecrossinggame.player import Player
from turtlecrossinggame.car_manager import CarManager
from turtlecrossinggame.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_cars()
    for each_car in car.all_cars:
        if each_car.distance(player) < 20:
            game_is_on = False
    if player.ycor() >= 280:
        car.increase_speed()
        player.reset_position()
        scoreboard.update_score()




screen.exitonclick()