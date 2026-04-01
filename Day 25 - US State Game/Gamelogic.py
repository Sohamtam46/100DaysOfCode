from turtle import Turtle
import pandas as pd


states_data = pd.read_csv("50_states.csv")



def check_answer(guess_name):

    if guess_name in states_data.state.values:
        return True
    return False

def state_name_show(guess_name):
    state_name = Turtle()
    state_name.hideturtle()
    state_name.penup()
    state_x_value = states_data[states_data["state"] == guess_name].x.values.item()
    state_y_value = states_data[states_data["state"] == guess_name].y.values.item()
    state_name.goto(x=state_x_value,y=state_y_value)
    state_name.write(f"{guess_name}")

