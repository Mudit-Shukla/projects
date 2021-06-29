from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 240)
        self.level = 1
        self.hideturtle()
        self.write_score()



    def update_score(self):
        self.level += 1
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Level : {self.level}", align= ALIGNMENT, font = FONT)


