from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import random


# Create Question Bank for Quiz
question_bank = []

for question in question_data:
    new_q = Question(question['text'], question['answer'])
    question_bank.append(new_q)

quiz = QuizBrain(question_bank)

while quiz.questions_remain():
    quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {quiz.score}/{len(question_bank)}")