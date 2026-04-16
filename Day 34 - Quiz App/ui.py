from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quizz_brain : QuizBrain):

        self.quizz = quizz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_Label = Label(text=f"Score : 0", bg=THEME_COLOR, fg="White")
        self.score_Label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.q_text = self.canvas.create_text(150, 125, text=f"Question",width=280, fill=THEME_COLOR, font=("Ariel", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_button_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_button_img, highlightthickness=0)
        self.true_button.grid(column=0, row=2)

        false_button_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_button_img, highlightthickness=0)
        self.false_button.grid(column=1, row=2)

        self.update_question()

        self.window.mainloop()

    def update_question(self):
        question = self.quizz.next_question()
        self.canvas.itemconfig(self.q_text,text=question)









