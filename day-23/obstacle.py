from turtle import Turtle
from random import randint
from player import Player

random_y = randint(-250,250)

class Obstacle(Turtle):
    def __init__(self):
        super().__init__()
        self.stretch_wid = 1
        self.stretch_len = 2
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=self.stretch_wid,stretch_len=self.stretch_len,outline=1)
        self.goto(414,random_y)
        
    def move(self):
        new_x = self.xcor() - 1
        if not self.xcor() < -418:
            self.setx(new_x)
            
    def detect_collision(self, object: Player):
        object_radius = 10
        
        car_half_height = self.stretch_wid * 10
        car_half_width = self.stretch_len * 10
        
        x_limit = car_half_width + object_radius
        y_limit = car_half_height + object_radius
        
        x_hit = abs(object.xcor() - self.xcor()) < x_limit
        y_hit = abs(object.ycor() - self.ycor()) < y_limit
        
        if x_hit and y_hit:
            return True
        return False