from turtle import Turtle
from ball import Ball

class Paddle(Turtle):
    def __init__(self, x, y=0):
        self.stretch_wid = 5
        self.stretch_len = 1
        super().__init__()
        self.shape("square")
        self.color("red", "white")
        self.penup()
        self.score = 0
        
        self.shapesize(stretch_wid=self.stretch_wid,stretch_len=self.stretch_len,outline=1)
        self.goto(x, y)
        
    def move_up(self):
        new_position = self.ycor() + 20
        if self.ycor() > 250:
            pass
        else:
            self.sety(new_position)
        
    def move_down(self):
        new_position = self.ycor() - 20
        if self.ycor() < -220:
            pass
        else:
            self.sety(new_position)
            
    def detect_collision(self, object: Ball):
        ball_radius = 10
        
        paddle_half_height = self.stretch_wid * 10
        paddle_half_width = self.stretch_len * 10
        
        x_limit = paddle_half_width + ball_radius
        y_limit = paddle_half_height + ball_radius
        
        x_hit = abs(object.xcor() - self.xcor()) < x_limit
        y_hit = abs(object.ycor() - self.ycor()) < y_limit
        
        if x_hit and y_hit:
            return True
        return False