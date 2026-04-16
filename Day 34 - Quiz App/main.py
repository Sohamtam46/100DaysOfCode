from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface



question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quizz_ui = QuizInterface(quiz)
quizz_ui.update_question()

# while quiz.still_has_questions():
#     q_text = quiz.next_question()
#     quizz_ui.update_question(q_text)

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
