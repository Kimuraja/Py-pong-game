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
    time.sleep(0.1)
    s.update()
    b.move()
    x, y = b.pos()
    if x > 285:
        b.bounce(position=+20)
    elif x < -285:
        b.bounce(position=-20)

s.exitonclick()
