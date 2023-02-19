from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor('black')
s.title("PONG GAME")
s.tracer(0)

HEIGHT = s.window_height()

p_r = Paddle((350, 0))
p_l = Paddle((-350, 0))
b = Ball()

s.listen()
s.onkey(p_r.go_up, "Up")
s.onkey(p_r.go_down, "Down")

s.onkey(p_l.go_up, "w")
s.onkey(p_l.go_down, "s")

is_on = True
while is_on:
    time.sleep(0.05)
    s.update()
    b.move()

    # Detect collision with wall
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()

    # Detect collision with paddle
    if b.distance(p_r) < 50 and b.xcor() > 320 or b.distance(p_l) < 50 and b.xcor() < -320:
        b.bounce_x()

    # Detect if the ball goes out of bounds at the edge of screen
    if b.xcor() > 380:
        b.reset_position()

    if b.xcor() < -380:
        b.reset_position()
s.exitonclick()
