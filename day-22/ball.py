from turtle import Turtle
import math, random

class Ball(Turtle):
    def __init__(self):
        self.directions = ["right", "left"]
        self.positions = ["top", "bottom"]
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.direction = random.choice(self.directions)
        self.position = random.choice(self.positions)
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
        self.forward(1)
        
        if self.ycor() > 280:
            self.setheading(self.heading() + 90)
        elif self.ycor() < -280:
            self.setheading(self.heading() + 90)
                    
    def change_direction(self):
        self.setheading(self.heading() - 90)
        
    def reallocate(self, was_hit: bool | None):
        self.home()
        if was_hit:
            pass
        else:
            if self.direction == "right":
                self.direction = "left"
                self.seth(180)
                self.position = random.choice(self.positions)
                if self.position == "top":
                    self.left(45)
                else:
                    self.right(45)
            else:
                self.direction = "right"
                self.seth(0)
                self.position = random.choice(self.positions)
                if self.position == "top":
                    self.right(45)
                else:
                    self.left(45)