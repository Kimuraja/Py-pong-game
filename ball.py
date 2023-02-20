from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("#ee6c4d")
        self.pu()
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.01

    def move(self):
        new_x = self.xcor() - self.x_move
        new_y = self.ycor() - self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_game(self):
        self.goto(0, 0)
        self.bounce_x()