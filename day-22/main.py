from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
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
    
    if player.score == max_score:
        game_over = True
        player_2_won = True
    elif opponent.score == max_score:
        game_over = True
        player_1_won = True
    
    if ball.xcor() > 380 or ball.xcor() < -385:
        if ball_was_hit_by_player:
            player.score += 1
            print("Player 2 score a point!")
            ball.reallocate()
        elif ball_was_hit_by_opponnet:
            opponent.score += 1
            print("Player 1 score a point!")
            ball.reallocate()
        else:
            ball.reallocate()
        
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