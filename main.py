from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(width=800, height=600)
s.bgcolor('#fffcf2')
s.title("PONG GAME")
s.tracer(0)

p_r = Paddle((350, 0))
p_l = Paddle((-350, 0))
b = Ball()
score = Scoreboard()


s.listen()
s.onkeypress(p_r.go_up, "Up")
s.onkeypress(p_r.go_down, "Down")

s.onkeypress(p_l.go_up, "w")
s.onkeypress(p_l.go_down, "s")

is_on = True
while is_on:

    # Speed can be changed by multiplying 'move_speed' by 0.9
    time.sleep(b.move_speed)
    s.update()
    b.move()

    # Detect collision with wall
    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()

    # Detect collision with paddle
    if b.distance(p_r) < 50 and b.xcor() > 320 or b.distance(p_l) < 50 and b.xcor() < -320:
        b.bounce_x()

    if b.xcor() > 370:
        b.reset_game()
        score.l_point()

    if b.xcor() < -370:
        b.reset_game()
        score.r_point()

    if score.r_score == 10 or score.l_score == 10:
        score.winner()
        is_on = False

s.exitonclick()
