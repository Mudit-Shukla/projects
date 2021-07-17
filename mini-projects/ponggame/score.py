from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.goto(0, 275)
        self.update_score_board()

    def update_player1_score(self):
        self.player1_score += 1
        self.update_score_board()

    def update_player2_score(self):
        self.player2_score += 1
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f" {self.player1_score}         {self.player2_score}",
                   align=ALIGNMENT, font=FONT)
