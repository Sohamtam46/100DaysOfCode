from tkinter import *
from tkinter import messagebox
import data
import random
import pyperclip
import json

# ---------------------------- SEARCH LOGIN INFO ------------------------------- #

def search_login_info():
    try:
        website = website_input.get()
        with open("login.json" , mode="r") as data_file:
            data = json.load(data_file)
            retrieved_email = data[website]["Email"]
            retrieved_password = data[website]["Password"]
            messagebox.showinfo(f"{website} Login Details",
                                message=f"Your Login Info is as follows:\nEmail : {retrieved_email}\nPassword : {retrieved_password}")
    except FileNotFoundError:
        messagebox.showerror("File Not Found", message="No login details saved yet.")
    except KeyError:
        messagebox.showerror("Error Retrieving Data",message=f"No Login Details for {website} found!")




# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_input.delete(0, END)
    password_list = []

    password_list += [random.choice(data.letters) for _ in range(2)]
    password_list += [random.choice(data.numbers) for _ in range(2)]
    password_list += [random.choice(data.symbols) for _ in range(2)]

    random.shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_login_data():

    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website : {
            "Email":email,
            "Password":password
        }
    }

    # validation for input fields
    if len(website) == 0:
        messagebox.showerror(title="Missing Data!", message="You haven't entered the website address! Please add.")
        website_input.focus()
    elif len(email) == 0:
        messagebox.showerror(title="Missing Data!", message="You haven't entered the email address! Please add.")
        email_input.focus()
    elif len(password) == 0:
        messagebox.showerror(title="Missing Data!",
                             message="You haven't entered the Password! Either generate or add one.")
        password_input.focus()
    else:
        messagebox.showinfo(title="Saved!", message="Your Login Details have been Saved!")

        try :
            with open("login.json", mode="r") as data_file:
                # Reading Data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("login.json", mode="w") as data_file:
                # write data
                json.dump(new_data, data_file, indent=4)

        else:
            # Update Data
            data.update(new_data)
            with open("login.json", mode="w") as data_file:
                # write data
                json.dump(data, data_file, indent=4)

        finally:
            # helps clear the inputs after saving the login data
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------ #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website")
website_label.grid(column=0, row=1)

website_input = Entry(width=30)
website_input.grid(column=1, row=1, sticky=W)
website_input.focus()

search_button = Button(text="Search", command=search_login_info,width=15)
search_button.grid(column=2, row=1)

email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)

email_input = Entry(width=52)
email_input.insert(0, "soham@gmail.com")
email_input.grid(column=1, row=2, columnspan=2, sticky=W)

password_label = Label(text="Password")
password_label.grid(column=0, row=3)

password_input = Entry(width=30)
password_input.grid(column=1, row=3, sticky=W)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=add_login_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
