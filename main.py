from turtle import Turtle,Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle =Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()







screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")


game_is_on= True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

#detection of wall collision
    if ball.ycor() > 280 or ball.ycor() < -280 :
        #needs to bounce he ball
        ball.bounce_y()

    #detect the colision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect misses of balls
    # this is r sided paddle miss
    if ball.xcor() >380:
        ball.reset_position()
        scoreboard.l_point()

    #this is l sided paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
