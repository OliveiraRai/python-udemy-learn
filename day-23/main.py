from turtle import Screen
from player import Player
from obstacle import Obstacle
from scoreboard import Scoreboard
from random import randint

obstacles: list[Obstacle] = []

screen = Screen()
screen.setup(width=800, height=600)

screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_forwards, "Up")

game_over = False

spawn_timer = 14
trigger = 15

def game_loop():
    global game_over, spawn_timer, trigger
    
    if player.ycor() > 280:
        scoreboard.update_score()
        player.reallocate()
    
    spawn_timer += 1
    if spawn_timer >= trigger:
        random_y = randint(-250,250)
        obstacles.append(Obstacle(random_y))
        spawn_timer = 0
    
    for obstacle in obstacles:
        if obstacle.detect_collision(player):
            game_over = True
            return
        obstacle.move(scoreboard.level)
        
    for obstacle in obstacles:
        if obstacle.out_of_screen():
            obstacle.hideturtle()
            obstacles.remove(obstacle)
    
    screen.update()
    
    if not game_over:
        screen.ontimer(game_loop, 16)

game_loop()
screen.mainloop()

screen.clear()
    
screen.exitonclick()