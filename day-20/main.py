from turtle import Turtle, Screen
import time, random

global segments

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()

distance = 21
new_direction = "right"
last_direction = ""
turn_coordinates = []
wasKeyPressed = False
screen.title("Snake Game")

class Snake():
    def __init__(self, starting_length=3):
        self.segments = []
        super().__init__()
        for _ in range(starting_length):
            new_segment = Turtle("square")
            new_segment.penup()
            self.segments.append(new_segment)
        for id, segment in enumerate(self.segments):
            segment.setposition((segment.xcor() - (id * distance), 0))
        screen.update()
        
    def add_snake_segment(self):
        new_segment = Turtle("square")
        new_segment.penup()
        self.segments.append(new_segment)
        
snake = Snake()

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5,outline=1)
        self.penup()
        
    def location_randomizer(self):
        random_x = random.randint(a=-280, b=280)
        random_y = random.randint(a=-280, b=280)
        random_location = (random_x, random_y)
        self.setposition(random_location)
        return self
    
    def collision_verifier(self, t1, t2, distance=13):
        if t1.distance(t2) < distance * 2:
            return True
        return False

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
        turn_coordinates.append({new_direction: snake.segments[0].pos()})
        # print(last_direction)
    
def goDown():
    global new_direction, turn_coordinates, last_direction
    if last_direction and new_direction == "down":
        return
    elif new_direction == "up":
        return
    else:
        last_direction = new_direction
        new_direction = "down"
        turn_coordinates.append({new_direction: snake.segments[0].pos()})
        # print(last_direction)
    
def goLeft():
    global new_direction, turn_coordinates, last_direction
    if last_direction and new_direction == "left":
        return
    elif new_direction == "right":
        return
    else:
        last_direction = new_direction
        new_direction = "left"
        turn_coordinates.append({new_direction: snake.segments[0].pos()})
        # print(last_direction)
    
def goRight():
    global new_direction, turn_coordinates, last_direction
    if last_direction and new_direction == "right":
        return
    elif new_direction == "left":
        return
    else:
        last_direction = new_direction
        new_direction = "right"
        turn_coordinates.append({new_direction: snake.segments[0].pos()})
        # print(last_direction)
    
game_is_on = True

was_food_created = False
while game_is_on:
    if not was_food_created:
        food = Food().location_randomizer()
        was_food_created = True
    else:
        s_head = snake.segments[0]
        if food.collision_verifier(s_head, food):
            # remove food
            food.location_randomizer()
            # adiciona +1 turtle
            snake.add_snake_segment()
        
    screen.onkeypress(goUp, "w")
    screen.onkeypress(goLeft, "a")
    screen.onkeypress(goDown, "s")
    screen.onkeypress(goRight, "d")
    
    turn_coordinates.append({new_direction: snake.segments[0].pos()})
    last_position = turn_coordinates[-1][new_direction]
    
    for segment in snake.segments:
        
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
    

## SNAKE INTERACION WITH FOOD
## FOOD LOCATION RANDOMIZATION
## COLLISION WITH WALLS
## COLLISION WITH SNAKE'S OWN BODY

screen.exitonclick()