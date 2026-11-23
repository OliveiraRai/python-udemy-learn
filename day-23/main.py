from turtle import Screen
from player import Player
from obstacle import Obstacle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

player = Player()
obstacle = Obstacle()

screen.listen()
screen.onkey(player.move_forwards, "Up")

game_over = False

while not game_over:
    screen.update()
    
    if player.ycor() > 280:
        game_over = True
    
    obstacle.move()
    time.sleep(0.016)
    
screen.exitonclick()