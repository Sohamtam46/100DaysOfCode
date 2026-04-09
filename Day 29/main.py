from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------ #

window = Tk()
window.title("Password Manager")
window.config(padx=100,pady=50)


canvas = Canvas(width=200,height=192)
logo_img =PhotoImage(file="logo.png")
canvas.create_image(100,112,image = logo_img)
canvas.grid(column=1,row=0)

website_label =Label(text="Website")
website_label.grid(column=0,row=1)

website_input = Entry(width=50)
website_input.grid(column=1,row=1)

email_label =Label(text="Email/Username")
email_label.grid(column=0,row=2)

email_input = Entry(width=50)
email_input.grid(column=1,row=2)

password_label =Label(text="password")
password_label.grid(column=0,row=3)

password_input = Entry(width=25)
password_input.grid(column=1,row=3,)

generate_pass_button = Button(text="Generate Password")
generate_pass_button.grid(column=2,row=3)

calculate_button = Button(text="Add",width=42)
calculate_button.grid(column=1,row=4)









window.mainloop()