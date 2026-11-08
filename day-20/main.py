from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()

segments = [] 
distance = 21
new_direction = "right"
last_direction = ""
turn_coordinates = []
wasKeyPressed = False
screen.title("Snake Game")

# Tecnically creates pieces that will be used
for _ in range(7):
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.penup()
    segments.append(new_segment)

# Creates the snake's body
for id, segment in enumerate(segments):
    segment.setposition((segment.xcor() - (id * distance), 0))
    
screen.update()

## FUNCTIONS

def goUp():
    global new_direction, turn_coordinates, last_direction
    if last_direction and new_direction == "up":
        return
    elif new_direction == "down":
        return
    else:
        last_direction = new_direction
        new_direction = "up"
        turn_coordinates.append({new_direction: segments[0].pos()})
        print(last_direction)
    
def goDown():
    global new_direction, turn_coordinates, last_direction
    if last_direction and new_direction == "down":
        return
    elif new_direction == "up":
        return
    else:
        last_direction = new_direction
        new_direction = "down"
        turn_coordinates.append({new_direction: segments[0].pos()})
        print(last_direction)
    
def goLeft():
    global new_direction, turn_coordinates, last_direction
    if last_direction and new_direction == "left":
        return
    elif new_direction == "right":
        return
    else:
        last_direction = new_direction
        new_direction = "left"
        turn_coordinates.append({new_direction: segments[0].pos()})
        print(last_direction)
    
def goRight():
    global new_direction, turn_coordinates, last_direction
    if last_direction and new_direction == "right":
        return
    elif new_direction == "left":
        return
    else:
        last_direction = new_direction
        new_direction = "right"
        turn_coordinates.append({new_direction: segments[0].pos()})
        print(last_direction)
    
## SNAKE MOVEMENT - DONE
## mover para direita não está funcionando.
## os testes apontam que last_direction nunca muda de valor e continua sendo "right"
game_is_on = True

while game_is_on:
    # atualiza valor de new_direction e salva a ultima direção em last_direction
    # também salva as coordenadas da ultima mudança de new_direction
    screen.onkeypress(goUp, "w")
    screen.onkeypress(goLeft, "a")
    screen.onkeypress(goDown, "s")
    screen.onkeypress(goRight, "d")
    
    turn_coordinates.append({new_direction: segments[0].pos()})
    last_position = turn_coordinates[-1][new_direction]
    
    for segment in segments:
        
        if segment.pos() == last_position:
            
            match new_direction:
                case "up":
                    segment.setposition((segment.xcor(), segment.ycor() + distance))
                case "down":
                    segment.setposition((segment.xcor(), segment.ycor() - distance))
                case "left":
                    segment.setposition((segment.xcor() - distance, segment.ycor()))
                case "right":
                    segment.setposition((segment.xcor() + distance, segment.ycor()))
                    
        else:
            new_position = segment.pos()  
            segment.setposition(last_position)
            last_position = new_position
            
    turn_coordinates = []
            
    screen.update()
    time.sleep(0.25)
    
## FOOD GENERATION 
## SNAKE INTERACION WITH FOOD
## FOOD LOCATION RANDOMIZATION
## COLLISION WITH WALLS
## COLLISION WITH SNAKE'S OWN BODY

screen.exitonclick()