from quizgame.Question import Question
from quizgame.data import questions
from quizgame.quiz_brain import QuizGame

question_bank = []
score = 0

for question in questions:
    text = question["text"]
    answer = question["answer"]
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz1 = QuizGame(question_bank)

while quiz1.stil_has_question():
    quiz1.next_question()
