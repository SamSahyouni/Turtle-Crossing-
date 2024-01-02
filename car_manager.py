# the CarManager class controls the cars for each level. They get faster and more frequent
# as the game progresses
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(COLORS[random.randint(0,5)])
        self.penup()
        self.shape("square")
        self.turtlesize(stretch_wid=2,stretch_len=1)
        self.setheading(90)
        self.goto(-300,random.randint(-280,280))

    def drive(self,movement):
        if self.xcor() < 320 and self.xcor() > -320:
            self.goto(self.xcor()+movement,self.ycor())

    def more_cars(self):
        roll_result = random.randint(1,6)
        if roll_result == 1:
            return True
        else:
            return False

    def reset(self):
        self.clear()
