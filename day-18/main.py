from turtle import Turtle, Screen
import math
from random import choice, randint

t = Turtle()
screen = Screen()
screen.setup(width=800, height=600)

### DRAWS SQUARE AND THEN CUTS THROUGH BOTH DIAGONALS USING SOME MATH

# side = 100
# right_angle = 90

# for _ in range(4):
#     t.forward(side)
#     t.right(right_angle)
    
# hipotenuse = math.sqrt(side**2 + side**2)

# t.right(right_angle/2)
# t.color("red")
# t.forward(hipotenuse)

# rotation = right_angle - (-(right_angle/2))
# t.color("black")
# t.left(rotation)
# t.forward(side)
# t.left(rotation)
# t.color("blue")
# t.forward(hipotenuse)

### DASHED LINE GENERATOR (DONE BY HAND AND IM VERY PROUD OF MYSELF LOL)

# t.hideturtle()

# def dashed(len, dashes):
#     isDown = True
#     blanks = dashes - 1
    
#     if blanks < 0:
#         return "Error: dashes cannot be 0 or less."
    
#     sections = dashes + blanks
#     dash_size = len / sections
    
#     for _ in range(sections):
#         if isDown:
#             t.pd()
#             t.fd(dash_size)
#             t.pu()
#             isDown = False
#         else:
#             t.fd(dash_size)
#             t.pd()
#             isDown = True
            
# dashed(100, 5)

### DRAWS EVERY GEOMETRIC FIGURE FROM TRIANGLE TO DECAGON (8 FIGURES)

# circumference = 360
# sides = 3
# side = 100
# t.teleport(x=-50,y=200)
# color_index = 0
# colors = [
#     "black",
#     "cornflowerblue", 
#     "forestgreen", 
#     "orchid", 
#     "tomato", 
#     "gold", 
#     "darkorchid", 
#     "darkorange",
# ]

# for _ in range(8):
#     t.color(colors[color_index])
#     angle = circumference / sides
#     for _ in range(sides):
#         t.fd(side)
#         t.right(angle)
#     color_index += 1
#     sides += 1

### RANDOM WALK ALGORITHM

## configuration
t.speed(7)
t.hideturtle()
t.pensize(10)
screen.colormode(255)

# random color generator
def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rgb = (r, g, b)
    return rgb

## variables
directions = [0, 90, 180, 270]

## logic
for _ in range(100):
    t.pencolor(random_color())
    t.setheading(choice(directions))
    t.forward(25)

screen.exitonclick()