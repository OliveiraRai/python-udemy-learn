from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()

### FUNCTIONS
def lookUp():
    for segment in segments:
        segment.setheading(90)
        
def lookLeft():
    for segment in segments:
        segment.setheading(180)
        
def lookDown():
    for segment in segments:
        segment.setheading(270)
        
def lookRight():
    for segment in segments:
        segment.setheading(0)

### BIGGER PROBLEM: SNAKE GAME
## INTO
### SMALLER PROBLEMS:
## SNAKE BODY

segments = []
distance = 21

### Tecnically creates pieces that will be used
for _ in range(3):
    new_segment = Turtle()
    new_segment.shape("square")
    new_segment.penup()
    segments.append(new_segment)

for id, segment in enumerate(segments):
    segment.setposition((segment.xcor() - (id * distance), 0))
    
screen.update()
    
## SNAKE MOVEMENT
game_is_on = True

while game_is_on:
    for segment in segments:
        segment.setposition((segment.xcor() - distance, 0))
    screen.update()
    time.sleep(0.25)
    
## FOOD GENERATION 
## SNAKE INTERACION WITH FOOD
## FOOD LOCATION RANDOMIZATION
## COLLISION WITH WALLS
## COLLISION WITH SNAKE'S OWN BODY

screen.exitonclick()