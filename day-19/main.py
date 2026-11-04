from turtle import Turtle, Screen
from random import choice, randint

# t = Turtle()
screen = Screen()
screen.setup(width=800, height=600)

## Playable line sketcher

# def forwards():
#     t.forward(25)
    
# def backwards():
#     t.backward(25)
    
# def rotateLeft():
#     new_heading = t.heading() + 10
#     t.setheading(new_heading)
    
# def rotateRight():
#     new_heading = t.heading() - 10
#     t.setheading(new_heading)
    
# def clearScreen():
#     t.reset()

# screen.listen()
# screen.onkey(forwards, "w")
# screen.onkey(backwards, "s")
# screen.onkey(rotateLeft, "a")
# screen.onkey(rotateRight, "d")
# screen.onkey(clearScreen, "c")

## Turtle Race

is_race_on = False
locations = [200, 100, 0, -100, -200]
colors = ["red", "green", "blue", "brown", "cyan"]
turtles = []

for i in range(0, 5):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[i])
    new_turtle.goto(-360, locations[i])
    turtles.append(new_turtle)
    
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win the race?")

if user_bet:
    is_race_on = True
    
while(is_race_on):
    for turtle in turtles:
        if turtle.xcor() > 380:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
                
        turtle.forward(randint(0,10))
        
                

screen.exitonclick()