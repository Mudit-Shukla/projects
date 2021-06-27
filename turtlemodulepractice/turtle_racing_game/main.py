from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width = 500, height = 400)
user_choice = screen.textinput(title= "Turtle race", prompt="Bet on you turtle")
colors = ["red", "green", "blue", "yellow","orange", "purple"]
all_turtle = []

for i in range(0,6):
    turtle_name = Turtle("turtle")
    turtle_name.penup()
    turtle_name.color(colors[i])
    turtle_name.goto(-235, -100 + (i*45))
    all_turtle.append(turtle_name)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() >= 230:
            is_race_on = False
            color = (turtle.pencolor())
            if color == user_choice:
                print(f"You won. {color} is the wining turtle")
            else:
                print(f"You lost. {color} is the winner")
        dist = random.randint(0,10)
        turtle.forward(dist)




screen.exitonclick()
