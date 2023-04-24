from turtle import Turtle

FONT = ('Courier', 80, 'normal')
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        # Left score
        self.goto(-100, 190)
        self.write(arg=self.l_score, align=ALIGNMENT, font=FONT)
        # Right score
        self.goto(100, 190)
        self.write(arg=self.r_score, align=ALIGNMENT, font=FONT)

    def update_left_score(self):
        self.l_score += 1
        self.show_score()

    def update_right_score(self):
        self.r_score += 1
        self.show_score()
