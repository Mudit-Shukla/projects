from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
XCOR = 300


class CarManager:


    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        lucky_number = random.choice(range(1, 7))
        if lucky_number == 1:
            car = Turtle("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            y_cor = random.randint(-240, 240)
            car.goto(XCOR, y_cor)
            car.setheading(180)
            self.all_cars.append(car)


    def move_cars(self):
        for car in self.all_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE, MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT