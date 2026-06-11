from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def title():
    return ("<h1>Guess a number between 0 and 9</h1>"
            "<img src = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDBucHJvbXJnNmlhemRydzYwNG83ejY1Ynd4Y28wYXluNW1uNDVzcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mcsPU3SkKrYDdW3aAU/giphy.gif'>")

random_num = random.randint(0,9)
print(random_num)

@app.route("/<int:user_guess>")
def guess_number(user_guess):
    if user_guess == random_num:
        return ("<h1>That's right!</h1>"
                "<img src = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExajhjNTF4ZGcyM3lzMXpob253OHB0Yzk0anU5MTk4NzNmbDVkMjkybSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MDJ9IbxxvDUQM/giphy.gif'>")
    elif user_guess > random_num:
        return ("<h1>Guess too high!</h1>"
                "<img src = 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnphd2hmaXQ4NXE3ODN4cjBrM3NsNHRpeWxtMXZ1ZmgweGc4Nno5YSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BBNYBoYa5VwtO/giphy.gif'>")
    else:
        return ("<h1>Guess too low!</h1>"
                "<img src = 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZG1qejU5eWpmdXBzaW5va3NlajF5ZWJkbW40eXR0N3o2NW1tZWZiOCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5i7umUqAOYYEw/giphy.gif'>")

if __name__ == "__main__":
    app.run(debug=True)
