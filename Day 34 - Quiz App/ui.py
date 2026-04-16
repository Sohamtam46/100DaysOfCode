from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quizz_brain : QuizBrain):

        self.quizz = quizz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_Label = Label(text=f"Score : 0", bg=THEME_COLOR, fg="White", font=("Ariel",10,"bold"))
        self.score_Label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.q_text = self.canvas.create_text(150, 125, text=f"Question",width=280, fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0, command = self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0, command = self.false_pressed)
        self.false_button.grid(column=1, row=2)

        # get the first question to show up
        self.update_question()

        self.window.mainloop()

    def update_question(self):
        self.canvas.config(bg="white")
        question = self.quizz.next_question()
        self.canvas.itemconfig(self.q_text,text=question)

    def true_pressed(self):
        is_right = self.quizz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quizz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_Label.config(text=f"Score : {self.quizz.score}")
        if self.quizz.still_has_questions():
            self.window.after(1000,func=self.update_question)
        else:
            self.window.after(1000,func=self.end_game)

    def end_game(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.q_text,text=f"That's the end of the Quizz!\nYou Scored : {self.quizz.score}!")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")










