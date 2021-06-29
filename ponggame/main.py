from turtle import Screen
from ponggame.paddle import Paddle
from ponggame.ball import Ball
from ponggame.score import ScoreBoard
import time

PLAYER1_POSITION = (350, 0)
PLAYER2_POSITION = (-350, 0)
SLEEPING_TIME = 0.1
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)


player1 = Paddle(PLAYER1_POSITION)
player2 = Paddle(PLAYER2_POSITION)
ball = Ball()
score_board = ScoreBoard()

game_is_on = True
screen.listen()

screen.onkeypress(player1.move_up, "Up")
screen.onkeypress(player1.move_down, "Down")
screen.onkeypress(player2.move_up, "5")
screen.onkeypress(player2.move_down, "2")


while game_is_on:
    time.sleep(SLEEPING_TIME)
    ball.move()
    if ball.ycor() >= 280:
        ball.bounce_y()
    if ball.ycor() <= -280:
        ball.bounce_y()
    if ball.distance(player1) < 50 and ball.xcor() > 340 :
        ball.bounce_x()
        SLEEPING_TIME /= 2
    if ball.distance(player2) < 50 and ball.xcor() < -340 :
        ball.bounce_x()
        SLEEPING_TIME /= 2
    if ball.xcor() < -350:
        ball.missed_ball()
        score_board.update_player2_score()
        if SLEEPING_TIME < 0.05:
            SLEEPING_TIME *= 2
    if ball.xcor() > 350:
        ball.missed_ball()
        score_board.update_player1_score()
        if SLEEPING_TIME < 0.05:
            SLEEPING_TIME *= 2
    screen.update()


screen.exitonclick()