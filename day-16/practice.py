# from turtle import Turtle, Screen

# turtle = Turtle()
# turtle.shape("turtle")
# turtle.color("chartreuse4")
# turtle.forward(15)

# my_screen = Screen()
# my_screen.window_height()
# my_screen.exitonclick()

from prettytable import PrettyTable

pokedex = [
    {
        "Pokemon": "Squirtle", 
        "Type": "Water",
    },
    {
        "Pokemon": "Charmander", 
        "Type": "Fire",
    },
    {
        "Pokemon": "Bulbasaur", 
        "Type": "Plant",
    },
    {
        "Pokemon": "Cyndaquil", 
        "Type": "Fire",
    },
    {
        "Pokemon": "Mudkip", 
        "Type": "Water",
    },
]

table = PrettyTable()
for x in range(1):
    table.add_column("Pokemon", [pokemon["Pokemon"] for pokemon in pokedex])
    table.add_column("Type", [pokemon["Type"] for pokemon in pokedex])

table.align = 'l'
print(table)