from tkinter import *

def button_clicked():
    print(user_input.get())
    km_data = int(user_input.get()) * 1.6
    km_value["text"] = int(km_data)

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=50,height=100)
window.config(padx=20,pady=20)


user_input = Entry()
user_input.grid(column=1,row=0)
user_input.focus()

miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

equal_to_label = Label(text="is equal to")
equal_to_label.grid(column=0,row=1)

km_value = Label(text="0")
km_value.grid(column=1,row=1)

km_label = Label(text="Km")
km_label.grid(column=2,row=1)

calculate_button = Button(text="Calculate",command=button_clicked)
calculate_button.grid(column=1,row=2)


window.mainloop()
