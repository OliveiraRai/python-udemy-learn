# class Question:
#     question_id = 0
#     option_id = 0
#     def __init__(self, text: str, answer: str, options=[]):
#         self.text = text
#         self.answer = answer
#         self.options = options
#         self.question_id += 1
        
#     def add_option(self, text):
#         self.option_id += 1
#         self.options.append({self.option_id: text})
        
#     def search_option_by_id(self, id: int):
#         for option in self.options:
#             for key in option:
#                 if key == id:
#                     return option[key]
#         return "Not found"
    
#     def guess_name(self, name: str):
#         for option in self.options:
#             for key in option:
#                 if option[key] == name:
#                     if name is self.answer:
#                         return f"Seu chute {name} está correto."
#                     else:
#                         return f"Seu chute {name} está incorreto."
#         return "Seu chute não é nenhuma das opções."
                
        
# question = Question("Qual o meu nome?", "Bolsonaro")
# question.add_option("Bolsonaro")
# question.add_option("Lula")
# print(f"O enunciado da questão é '{question.text}'.")
# print(f"O ID da questão é: {question.question_id}.")
# print(f"Opções: {question.options}")
# id = 2
# option = question.search_option_by_id(id)
# print(f"A opção de id {id} é: {option}.")
# guess = "Bolsonaro"
# guessed_correctly = question.guess_name(guess)
# print(guessed_correctly)

# agora é o problema que foi passado realmente
# acima é apenas esquizofrenia
class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer