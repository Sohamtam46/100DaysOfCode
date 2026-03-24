class QuizBrain:

    def __init__(self,q_list):
        self.q_num = 0
        self.q_list = q_list
        self.score = 0

    def next_question(self):
        question  = self.q_list[self.q_num].question
        user_ans = input(f"Q.{self.q_num + 1}: {question}(True/False)?:").lower()
        self.check_answer(user_ans,self.q_list[self.q_num].answer)
        self.q_num += 1

    def still_has_questions(self):
        return self.q_num < len(self.q_list)

    def check_answer(self,user_ans,actual_answer):
        if user_ans.lower() == actual_answer.lower():
            print("Correct Answer!")
            self.score += 1
        else:
            print("That's wrong answer")
        print(f"Correct answer is {actual_answer}.")
        print(f"Your current score is :{self.score}/{self.q_num + 1}.")
        print("\n"*2)


