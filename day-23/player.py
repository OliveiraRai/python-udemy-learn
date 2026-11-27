from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.seth(90)
        self.goto(0,-280)
        
    def move_forwards(self):
        self.forward(4)
        
    def reallocate(self):
        self.goto(0,-280)