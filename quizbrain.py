
class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list

    def get_question_number(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. #{self.question_number}: {current_question.text} (True/False)? ")