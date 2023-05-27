from colorama import Fore

class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number]
        print(f"Q{self.question_number+1}.- {question.text}")
        answer = input("Escribe 'True' si es Verdadero  o 'False' si es Falso: ")
        while self.check_answer_typed(answer)==False:
            answer = input("Escribe una opcion valida: ")
        self.check_answer(answer, question.answer)
        self.question_number+=1

    def still_has_questions(self):
        if self.question_number<len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower()==correct_answer.lower():
            print(Fore.GREEN + "Correcto!")
            self.score+=1
        else:
            print(Fore.RED + "Incorrecto")
        print(Fore.WHITE + f"Tu puntuacion actual es: {self.score}/{len(self.question_list)}")
        print("\n")

    def check_answer_typed(self, user_asnwer):
        if user_asnwer.lower()=="false" or user_asnwer.lower()=="true":
            return True
        else:
            return False
