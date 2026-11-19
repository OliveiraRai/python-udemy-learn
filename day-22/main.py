from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

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
scoreboard = Scoreboard()

# MOVEMENT

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(opponent.move_up, "w")
screen.onkey(opponent.move_down, "s")

# GAME

game_over = False
ball_was_hit_by_player = False
ball_was_hit_by_opponnet = False
player_1_won = False
player_2_won = False
max_score = 11

while not game_over:
    time.sleep(0.0016)
    screen.update()
    
    if scoreboard.r_score == max_score:
        game_over = True
        player_2_won = True
    elif scoreboard.l_score == max_score:
        game_over = True
        player_1_won = True
    
    if ball.xcor() > 380 or ball.xcor() < -385:
        if ball_was_hit_by_player:
            scoreboard.r_score += 1
            scoreboard.update_score()
            ball_was_hit_by_player = False
            ball.reallocate(was_hit=ball_was_hit_by_player)
        elif ball_was_hit_by_opponnet:
            scoreboard.l_score += 1
            scoreboard.update_score()
            ball_was_hit_by_opponnet = False
            ball.reallocate(was_hit=ball_was_hit_by_opponnet)
        else:
            ball.reallocate(was_hit=None)
        
    if player.detect_collision(object=ball):
        ball.change_direction()
        ball_was_hit_by_player = True
        ball_was_hit_by_opponnet = False
    elif opponent.detect_collision(object=ball):
        ball.change_direction()
        ball_was_hit_by_opponnet = True
        ball_was_hit_by_player = False
    
    ball.move()
    
sys = Turtle()
sys.color("white")
if player_1_won:
    sys.write("PLAYER 1 HAVE WON", align="center", font=("Arial", 24, "bold"))
else:
    sys.write("PLAYER 2 HAVE WON", align="center", font=("Arial", 24, "bold"))

screen.exitonclick()

## TODO INDICADOR VISUAL DE PONTUAÇÃO
## TODO LINHA QUE SEPARA O BOARD NO MEIO