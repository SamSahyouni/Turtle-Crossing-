# The Scoreboard class uses the Turtle to write the score as the game is played
# and save high scores

from turtle import Turtle,Screen
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score = 1
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0,240)
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(0,240)
        self.write(align="center",font=FONT,arg=f"Level:{self.score} High Score:{self.high_score}")

    def level_up(self):
        self.score += 1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
            self.screen = Screen()
            high_score_name = self.screen.textinput(title="New High Score!",prompt="Enter your name:\n")
            with open("high_score_names.txt", mode="a") as file:
                file.write(f"\n{high_score_name}:{self.high_score}")
            self.score = 0
        with open("high_score_names.txt") as file:
            high_scores = file.read()
        self.write(align="center", font=("Courier", 36, "normal"), arg=f"GAME OVER\n{high_scores}")




