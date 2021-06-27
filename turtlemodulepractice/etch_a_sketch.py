from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def turn_right():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear_screen():
    tim.penup()
    tim.clear()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, 'd')
screen.onkey(move_backward, 'a')
screen.onkey(turn_right, 'w')
screen.onkey(turn_left, 's')
screen.onkey(clear_screen, 'space')

screen.exitonclick()