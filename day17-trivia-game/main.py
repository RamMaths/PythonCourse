from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

#filling a list with question objects
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

#creating a QuizBrain object
quiz = QuizBrain(question_bank)

#starting the game
while quiz.still_has_questions()==True:
    quiz.next_question()

#finishing the game
print(f"Completaste la trivia...\nTu puntuacion final es: {quiz.score}/{len(question_bank)}")
