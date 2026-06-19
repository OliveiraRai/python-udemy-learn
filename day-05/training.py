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

