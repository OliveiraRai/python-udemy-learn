import random

# sum = 0
# for number in range(1, 101):
#     sum += number

# print(sum)

# for n in range(0, 100, 3):
#     print(n)

# for n in range(1, 101):
#     if n % 3 == 0 and n % 5 == 0:
#         print("FizzBuzz")
#     elif n % 5 == 0:
#         print("Buzz")
#     elif n % 3 == 0:
#         print("Fizz")
#     else:
#         print(n)

### base list
# scores = [136, 134, 85, 138, 151, 76, 158, 128, 78, 186, 122, 156, 166, 81, 125, 142, 177, 93,
#           108, 145, 126, 91, 141, 124, 149, 152, 168, 167, 146, 137]
### max module remaking
# max = 0
# for score in scores:
#     if score > max:
#         max = score

# print(f"Maximum value: {max}")

### min module remaking
# min = max
# for score in scores:
#     if score < min:
#         min = score

# print(f"Mininum value: {min}")

# ### sum module remaking
# sum = 0
# for score in scores:
#     sum += score

# print(f"Sum: {sum}")

# ### len module remaking
# len = 0
# for score in scores:
#     len += 1

# print(f"Length: {len}")

### SORTING ALGORITHM
### IT WORKS, BUT SHUFFLES TOO MANY TIMES THAN NEEDED
# my_list = [2, 8, 5, 3, 9, 1, 4]

# for index, item in enumerate(my_list):
#     for i, current in enumerate(my_list):
#         if i < index: 
#             continue
#         if my_list[i] < my_list[index]:
#             print(f"dad: {my_list[index]} - son: {my_list[i]} - lesser: TRUE")
#             my_list[index], my_list[i] = my_list[i], my_list[index]
#             print(f"updated list {my_list}")
#         else:
#             print(f"dad: {my_list[index]} - son: {my_list[i]} - lesser: FALSE")
#     print("================================")

# print(f"Final list: {my_list}")

### try later to make sorting algorithm better cuz it shuffles too much

### avg module making
# sorted_list = my_list
# list_avg = 0
# sum = 0
# list_length = len(sorted_list)
# for i in sorted_list:
#     sum += i

# list_avg = sum / list_length
# print(list_avg)

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