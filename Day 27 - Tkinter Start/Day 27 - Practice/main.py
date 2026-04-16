from tkinter import *

# Button Function
def button_clicked():
    i = input.get()
    my_label["text"] = i

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)

# Label
my_label = Label(text="I am a Label", font=("Arial",24,"bold"))
# ways to display the widgets : [CANT USE PACK AND GRID TOGETHER]
# my_label.pack()
# my_label.place(x=0,y=150)
my_label.grid(column=0,row=0)

# property update using config or accessing properties
# my_label.config(text="New text")
# my_label["text"] = "even newer text"

# Button call
button = Button(text="Click me!",command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="Click me again!")
new_button.grid(column=2,row=0)

# Entry (input)
input = Entry(width=10)
input.grid(column=3,row=2)












window.mainloop()
