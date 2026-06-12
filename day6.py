### did reeborg's world (website) challenges from hurdle 1 to 4 - and the maze one too
## hurdle 1 solution:

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()

## hurdle 2

# the code from hurdle 1 can be used here

## hurdle 3

# the code from hurdle 2 can be used here

## hurdle 4 - can be used in the last 3 hurdles

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def jump():
#     turn_left()
#     while wall_on_right():
#         move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     while front_is_clear():
#         move()
#     turn_left()

# while not at_goal():
#     if front_is_clear():
#         move()
#     else:
#         jump()

## maze

# def turn_right():
#     turn_left()
#     turn_left()
#     turn_left()
    
# def win():
#     while not at_goal():
#         if not wall_on_right():
#             turn_right()
#             move()
#         elif front_is_clear():
#             move()
#         else:
#             turn_left()

# win()

### In the maze challenge, there is a solvable bug where the character stays in a certain
### location and position, it can get you into a infinite loop. I cannot do this with my
### knowledge now, but I'll certainly solve it later!

## bug solution: