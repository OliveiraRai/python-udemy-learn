from turtle import Turtle
from random import randint

random_y = randint(-250,250)

class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1,stretch_len=2,outline=1)
        self.goto(414,random_y)
        
    def move(self):
        new_x = self.xcor() - 1
        if not self.xcor() < -418:
            self.setx(new_x)