from question_model import Question
from quiz_brain import QuizBrain
from data import question_data
import random


# Create Question Bank for Quiz
question_bank = []

for question in question_data:
    new_q = Question(question['text'], question['answer'])
    question_bank.append(new_q)

new_quiz = QuizBrain(question_bank)

while new_quiz.questions_remain():
    user_input = new_quiz.next_question()
    new_quiz.check_answer(user_input)
    