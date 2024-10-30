from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    q_bank = Question(question["question"], question["answer"])
    question_bank.append(q_bank)
print(question_bank[1].text)