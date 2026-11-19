from turtle import Screen
from paddle import Paddle
from ball import Ball
import math, time

# SETUP

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# OBJECT CREATION

player = Paddle(350)
opponent = Paddle(-350)
ball = Ball()

# MOVEMENT

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(opponent.move_up, "w")
screen.onkey(opponent.move_down, "s")

# GAME

game_over = False

while not game_over:
    time.sleep(0.0016)
    screen.update()
    if ball.xcor() > 380 or ball.xcor() < -385:
        game_over = True
        
    if player.detect_collision(object=ball) or opponent.detect_collision(object=ball):
        ball.change_direction()
    
    ball.move()

screen.exitonclick()