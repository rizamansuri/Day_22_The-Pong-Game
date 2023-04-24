# BismillahirRahmanirRahim
from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title(".....Riza's Arcade Pong Game.....")
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # Detect collision with wall
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(right_paddle) < 50 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if right paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_left_score()

    # Detect if left paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.update_right_score()

screen.exitonclick()
