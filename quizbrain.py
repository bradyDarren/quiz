import html

class QuizBrain:

    def __init__(self, q_list) -> None:
        self.question_number = 0
        self.question_list = q_list
        self.answers_correct = 0

    def remaining_questions(self):
        if self.question_number >= len(self.question_list): 
            return False
        else: 
            return True

    def get_next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_texts = html.unescape(self.current_question.text)
        return f"Q. #{self.question_number}: {q_texts} (True/False)?"
        # user_answer = input(f"Q. #{self.question_number}: {q_text} (True/False)? ").lower().strip()
        # self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.answers_correct += 1
            return True
        else: 
            return False
    
    def final_score(self, number_correct, number_of_questions):
        print("You have completed the quiz")
        print(f"Your final score was {number_correct}/{number_of_questions}")

