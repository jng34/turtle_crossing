from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def add_score(self):
        self.level += 1
        self.update_level()