from turtle import Screen
from paddle import Paddle_right, Paddle_left

s = Screen()
s.setup(width=800, height=600)
s.bgcolor('black')
s.title("PONG GAME")
s.tracer(0)

p_r = Paddle_right()
p_l = Paddle_left()

s.listen()
s.onkey(p_r.go_up, "Up")
s.onkey(p_r.go_down, "Down")

s.onkey(p_l.go_up, "w")
s.onkey(p_l.go_down, "s")



is_on = True
while is_on:
    s.update()

s.exitonclick()
