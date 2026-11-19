from turtle import Turtle
import math, random

# arctan = math.degrees(math.atan2(300, 400))
angle = 360

class Ball(Turtle):
    def __init__(self):
        directions = ["right", "left"]
        positions = ["top", "bottom"]
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.direction = "left"
        self.position = "bottom"
        if self.direction == "right":
            if self.position == "top":
                self.left(45)
            else:
                self.right(45)
        else:
            self.seth(180)
            if self.position == "top":
                self.right(45)
            else:
                self.left(45)
        
    def move(self):
        self.forward(.5)
        
        if self.ycor() > 280:
            self.setheading(self.heading() + 90)
        elif self.ycor() < -280:
            self.setheading(self.heading() + 90)
                    
    def change_direction(self):
        self.setheading(self.heading() - 90)