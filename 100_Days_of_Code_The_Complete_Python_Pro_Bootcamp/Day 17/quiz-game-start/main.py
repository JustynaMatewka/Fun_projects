from question_model import Question     #   Class - Question -> modify data from data.py
from data import question_data          #   Game database
from quiz_brain import QuizBrain        #   Class - QuizBrain ->

question_bank = []
for question in question_data:
    new_question = Question(question['text'], question['answer'])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
