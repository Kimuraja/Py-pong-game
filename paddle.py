from turtle import Turtle
PAD_R = Turtle()
PAD_L = Turtle()

class Paddle_right:
    def __init__(self):
        self.pad_r()

    def pad_r(self):
        PAD_R.shape("square")
        PAD_R.color("white")
        PAD_R.shapesize(stretch_wid=5, stretch_len=1)
        PAD_R.pu()
        PAD_R.goto(x=350, y=0)

    def go_up(self):
        new_y = PAD_R.ycor() + 20
        PAD_R.goto(PAD_R.xcor(), new_y)

    def go_down(self):
        new_y = PAD_R.ycor() - 20
        PAD_R.goto(PAD_R.xcor(), new_y)

class Paddle_left:
    def __init__(self):
        self.pad_l()

    def pad_l(self):
        PAD_L.shape("square")
        PAD_L.color("white")
        PAD_L.shapesize(stretch_wid=5, stretch_len=1)
        PAD_L.pu()
        PAD_L.goto(x= -350, y=0)

    def go_up(self):
        new_y = PAD_L.ycor() + 20
        PAD_L.goto(PAD_L.xcor(), new_y)

    def go_down(self):
        new_y = PAD_L.ycor() - 20
        PAD_L.goto(PAD_L.xcor(), new_y)