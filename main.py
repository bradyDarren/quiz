from data import question_data
from question_model import Question
from quizbrain import QuizBrain
from ui import QuizInterface

question_bank = []

for question in question_data:
    q_bank = Question(question["question"], (question["correct_answer"]).lower())
    question_bank.append(q_bank)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface()

# while quiz.remaining_questions():
#     quiz.get_next_question()
quiz.final_score(quiz.answers_correct, quiz.question_number)