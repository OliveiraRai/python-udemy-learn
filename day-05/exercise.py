# ### PASSWORD GENERATOR
# ## variables
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "=", "?", "@", "[", "]", "^", "_", "{", "}", "~"]
i = 0
password = []

### program initiation
print("Welcome to the non-byPassword Generator")
q = int(input("How many characters would you like in your password?\n"))
s = int(input("And how many symbols would you like?\n"))
n = int(input("And how many number?\n"))

### final quantity of each calculus
q = q - s - n

### character randomizer for each
## letters
while i < q:
    rand = random.randint(0, len(letters) - 1)
    letter = letters[rand]
    password.append(letter)

    # auto-increment
    i += 1

i = 0

## symbols
while i < s:
    rand = random.randint(0, len(symbols) - 1)
    symbol = symbols[rand]
    password.append(symbol)

    i += 1

i = 0

## numbers
while i < n:
    rand = random.randint(0, len(numbers) - 1)
    number = numbers[rand]
    password.append(number)

    i += 1 

### shuffling
random.shuffle(password)
result = "".join(password)

print(f"Your password: {result}")

## could've used random.choice() instead of using 3 lines of code