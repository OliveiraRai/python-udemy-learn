# def my_function():
#     return 3 * 2

# output = my_function()
# print(output)

# def format_name(f_name, l_name):
#     f_name = f_name.title()
#     l_name = l_name.title()
#     return f_name + " " + l_name

# print(format_name("jOhN", "pORk"))

# def function1(txt):
#     return txt + txt

# def function2(txt):
#     return txt.title()

# # um truque legal é olhar - nessa linha - 'function1("fun")' não como está escrito
# # mas enxergá-la com o que ela retorna. Não podemos ver, mas ali, ela não é mais 
# # 'function1("fun")', e sim: a string 'funfun'. e.g. como se a função também fosse
# # executá-da na nossa cabeça.
# print(function2(function1("fun"))) 

# def is_leap_year(year):
#     flag = False
#     if year % 4 == 0:
#         flag = True
#         if year % 100 == 0:
#             flag = False
#             if year % 400 == 0:
#                 flag = True
                
#     return flag
        
# print(is_leap_year(2000))
# print(is_leap_year(2100))
# print(is_leap_year(2024))

x = """Isso 
é
docstring
"""

print(x)

