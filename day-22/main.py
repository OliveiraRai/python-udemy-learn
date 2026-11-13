from turtle import Turtle, Screen, tracer

# SETUP

screen = Screen()
screen.setup(width=800, height=500)
screen.bgcolor("black")
screen.listen()
tracer(0)

screen.exitonclick()