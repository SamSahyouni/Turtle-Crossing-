# The Player class allows the user to move their turtle forward through each level
from turtle import Turtle,Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def listen(self):
        screen = Screen()
        screen.listen()
        screen.onkey(fun=self.move, key="Up")

    def move(self):
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.clear()
        self.goto(STARTING_POSITION)