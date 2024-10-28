from data import question_data
from question_model import Question

question_bank = []

for question in question_data:
    q_bank = Question(question["question"], question["answer"])
    question_bank.append({f"Question: {q_bank.text} : Answer: {q_bank.answer}"})
print(question_bank)