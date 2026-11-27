from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-370,250)
        self.pendown()
        self.write(arg=f"LEVEL {self.level}", font=("courier", 20, "normal"))
        self.penup()
        
    def update_score(self):
        self.level += 1
        self.clear()
        self.pendown()
        self.write(arg=f"LEVEL {self.level}", font=("courier", 20, "normal"))
        self.penup()
        