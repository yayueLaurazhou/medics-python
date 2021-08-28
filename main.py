from question_model import Question
from data import question_data
from questionnaire import Questionnaire

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

q = Questionnaire(question_bank)

while q.still_has_questions():
    q.next_question()

print("Congratulations! You've completed the health questionnaire.")
print(f"Your final score is: {q.score}/{q.question_number}")
if q.score > 8:
    print("Wow! Great job on keeping up a healthy lifestyle!")
elif q.score > 4:
    print("Overall you live a healthy life. Keep going!")
else:
    print("Oops! You really messed up with your life.")
