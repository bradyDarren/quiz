
class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list

    def remaining_questions(self):
        if self.question_number > len(self.question_list): 
            return False
        else: 
            return True

    def get_next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. #{self.question_number}: {current_question.text} (True/False)? ")
        correct = 0
        if user_answer == current_question.answer:
            correct += 1
            print("You got it correct")
            print(f"The correct answer was {current_question.answer}.")
            print(f"Your current score is: {correct}/{self.question_number}.")