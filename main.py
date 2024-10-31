from data import question_data
from question_model import Question
from quizbrain import QuizBrain

question_bank = []

for question in question_data:
    q_bank = Question(question["question"], question["answer"])
    question_bank.append(q_bank)

check = QuizBrain(question_bank)

for question in question_bank:
    check.get_question_number()