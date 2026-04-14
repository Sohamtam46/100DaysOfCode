from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
LANG1 = "Irish"
LANG2 = "English"

# ---------------------------- Flip the card  ------------------------------- #
def flip_the_card(chosen_word):
    canvas.itemconfig(card_img,image=flash_card_back_img)
    canvas.itemconfig(title_text,fill="white",text=LANG2)
    canvas.itemconfig(word_text,fill="white",text=chosen_word[LANG2])
    window.after_cancel(timer)

def remove_word():

    lang_words_dict.remove(chosen_word)
    words_to_learn = lang_words_dict
    words_to_learn_df=pd.DataFrame(words_to_learn)
    words_to_learn_df.to_csv("./data/words_to_learn.csv",index=False)
    new_word_generate()

# ---------------------------- New Word Generation ------------------------------- #
def new_word_generate():
    global chosen_word,timer
    chosen_word = random.choice(lang_words_dict)
    # getting hold of the word in first language / language to be learnt
    lang1_display_word = chosen_word[LANG1]
    canvas.itemconfig(card_img, image=flash_card_front_img)
    canvas.itemconfig(title_text,fill="black",text=LANG1)
    canvas.itemconfig(word_text,fill="black",text=lang1_display_word)
    timer = window.after(3000,flip_the_card,chosen_word)

# ---------------------------- UI SETUP ------------------------------ #

window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,background=BACKGROUND_COLOR)

try:
    lang_words = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    lang_words = pd.read_csv("./data/Irish_words.csv")

lang_words_dict = lang_words.to_dict(orient="records")
chosen_word = {}


canvas = Canvas(width=800,height=528,background=BACKGROUND_COLOR,highlightthickness=0)
flash_card_front_img = PhotoImage(file="./images/card_front.png")
flash_card_back_img = PhotoImage(file="./images/card_back.png")
card_img = canvas.create_image(410,270,image = flash_card_front_img)
title_text = canvas.create_text(400,150,text=f"{LANG1}",fill="black",font=(FONT_NAME,40,"italic"))
word_text = canvas.create_text(400,263,text=f"Press Red to Start",fill="black",font=(FONT_NAME,60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)
new_word_generate()

right_button_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_image, command=remove_word, highlightthickness=0)
right_button.grid(column=1,row=1)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, command=new_word_generate, highlightthickness=0)
wrong_button.grid(column=0,row=1)





window.mainloop()