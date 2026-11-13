from turtle import Turtle, Screen, tracer

# SETUP

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.listen()
tracer(0)

# VARIABLES

left_defense = -370
right_defense = 370
player_distance = 5
opponent_distance = 0.1

# SCREEN DIVISOR
def draw_screen_divisor(dashes_quantity: int):
    designer = Turtle("square")
    designer.hideturtle()
    designer.pensize(10)
    designer.color("white")
    designer.penup()
    designer.goto(x=0, y=250)
    offset = 500 // (dashes_quantity * 2 - 1)
    for _ in range(dashes_quantity):
        designer.pendown()
        designer.goto(x=0, y=designer.ycor() - offset)
        designer.penup()
        designer.goto(x=0, y=designer.ycor() - offset)
    
draw_screen_divisor(8)
screen.update()

# PLAYER

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_len=0.8, stretch_wid=3, outline=1)
        self.goto(x=left_defense, y=0)
        self.score = 0
        screen.update()
        
    def move_up(self):
        if self.ycor() > 219:
            pass
        else:
            self.goto(x=left_defense, y=self.ycor() + player_distance)
        screen.update()
        

    def move_down(self):
        if self.ycor() < -210:
            pass
        else:
            self.goto(x=left_defense, y=self.ycor() - player_distance)
        screen.update()
        
    
player = Player()
    
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")

# OPPONENT

class Opponent(Player):
    def __init__(self):
        super().__init__()
        self.goto(x=right_defense, y=0)
        self.direction = "down"  
        screen.update()      
        
    def movement(self):
        match self.direction:
            case "up":
                self.goto(x=right_defense, y=self.ycor() + opponent_distance)
                screen.update()
                if self.ycor() > 219:
                    self.direction = "down"
            case "down":
                self.goto(x=right_defense, y=self.ycor() - opponent_distance)
                screen.update()
                if self.ycor() < -210:
                    self.direction = "up"
        
opponent = Opponent()

# PONG BALL
class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_len=0.5, stretch_wid=0.5, outline=1)
        screen.update()
        
pong = PongBall()

screen.exitonclick()