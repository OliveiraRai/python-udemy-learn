from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.goto(-50,230)
        self.pendown()
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.penup()
        self.goto(50,230)
        self.pendown()
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))
        self.penup()
        
    def update_score(self):
        self.clear()
        self.goto(-50,230)
        self.pendown()
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.penup()
        self.goto(50,230)
        self.pendown()
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))
        self.penup()