class QuizGame:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        result = input(f"Q.{self.question_number} {current_question.text}(True/False)")
        output = self.check_answer(result, str(current_question.answer))
        self.update_score(output)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.capitalize() == correct_answer.capitalize():
            return True
        return False

    def stil_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        return False

    def update_score(self, output):
        if output:
            self.score += 1
        print(f"Your score is {self.score}/{self.question_number}")