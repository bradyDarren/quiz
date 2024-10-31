
class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.answers_correct = 0

    def remaining_questions(self):
        if self.question_number > len(self.question_list): 
            return False
        else: 
            return True

    def get_next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q. #{self.question_number}: {current_question.text} (True/False)? ").lower().strip()
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            self.answers_correct += 1
            print("You got it correct.")
        else: 
            print("Sorry, you are incorrect.")
        print(f"The correct answer was {correct_answer}.")
        print(f"Your current score is: {self.answers_correct}/{self.question_number}.")
        print("\n")
            

