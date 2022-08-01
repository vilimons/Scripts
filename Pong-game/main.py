from turtle import Turtle, Screen
import turtle
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((450, 0))
l_paddle = Paddle((-450, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")




game_is_on = True

while game_is_on:
    time.sleep(0.10)
    screen.update()
    ball.move()

    # Detect Collision with wall.
    if ball.ycor() > 380 or ball.ycor() < -380:
        ball.bounce_y()

    # Detect Collision with right paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 425:
        ball.bounce_x()
    # Detect Collision with left paddle.
    if ball.distance(l_paddle) < 50 and ball.xcor() < -425:
        ball.bounce_x()

    # Detect R Paddle misses:
    if ball.xcor() > 470:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L Paddle misses:
    if ball.xcor() < -470:
        ball.reset_position()
        scoreboard.r_point()
    









screen.exitonclick()