from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for entry in question_data:
    new_question = Question(entry["question"], entry["correct_answer"])
    question_bank.append(new_question)

quizz = QuizBrain(question_bank)

while quizz.still_has_questions():
    quizz.next_question()
print("You've completed the quiz!")
print(f"Your final score is {quizz.score}/{len(quizz.q_list)}")