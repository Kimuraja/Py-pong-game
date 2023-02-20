from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("#eb5e28")
        self.pu()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.updt_score()

    def updt_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.updt_score()

    def r_point(self):
        self.r_score += 1
        self.updt_score()