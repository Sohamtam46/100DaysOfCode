from flask import Flask

app = Flask(__name__)

def make_bold(function):
    def wrapper():
        original_string = function()
        return f"<b>{original_string}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye!!"

@app.route("/<name>")
def hello(name):
    return (f"<h1 align=center>Hello there {name}<h1>"
            f"<img src = 'https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExNDBucHJvbXJnNmlhemRydzYwNG83ejY1Ynd4Y28wYXluNW1uNDVzcyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/mcsPU3SkKrYDdW3aAU/giphy.gif'>")


if __name__ == "__main__":
    app.run(debug=True)

# learning decorators
# def hello_decorator(function):
#     def wrapper(*args,**kwargs):
#         print("Hello")
#         return function(*args,**kwargs)
#     return wrapper
#
#
# @hello_decorator
# def add (n1,n2):
#     return n1 + n2
#
# def sub (n1,n2):
#     return n1 - n2
#
# def multiply (n1,n2):
#     return n1 * n2
#
# def cal(cal_func,n1,n2):
#     return cal_func(n1,n2)
# #
# # result = cal(multiply,4,2)
# # print(result)
#
#
#
# result = add(2,4)
# print(result)