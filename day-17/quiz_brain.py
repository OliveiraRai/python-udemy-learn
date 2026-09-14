class QuizBrain:
    # construtor
    def __init__(self, questions_list: list):
        self.questions_list = questions_list
        self.question_number = 0
        self.score = 0
        
    def next_question(self):
        # pega question usando 'question_number' como índice para 'question_list'
        question = self.questions_list[self.question_number]
        # aqui, curiosamente, a variável se comporta diferentemente tanto para a linha cima quanto para a de baixo
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False)?: ").strip().capitalize()
        self.check_answer(user_answer, question.answer)
        
    def still_has_questions(self):
        # retorna booleano
        return len(self.questions_list) > self.question_number
    
    def check_answer(self, u_answer, q_answer):
        if u_answer == q_answer:
            print("You got it right!")
            self.score += 1
        else:
            print(f"You got it wrong!\nThe right answer was: {q_answer}")
        print(f"Your current score is: {self.score}/{len(self.questions_list)}")