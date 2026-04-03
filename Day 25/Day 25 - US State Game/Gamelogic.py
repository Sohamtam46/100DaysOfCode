from turtle import Turtle
import pandas as pd


states_data = pd.read_csv("50_states.csv")
all_states = states_data.state.to_list()



def check_answer(guess_name):

    if guess_name in states_data.state.values:
        return True
    return False

def state_name_show(guess_name):
    state_name = Turtle()
    state_name.hideturtle()
    state_name.penup()
    state_x_value = states_data[states_data["state"] == guess_name].x.item()
    state_y_value = states_data[states_data["state"] == guess_name].y.item()
    state_name.goto(x=state_x_value,y=state_y_value)
    state_name.write(f"{guess_name}")

# generate states forgotten by user  onto a csv
def game_over(answer_list):
    # states_not_guessed = []
    # states_not_guessed = list(set(all_states) - set(answer_list))
    # using list comprehension
    states_not_guessed = [state for state in all_states if state not in answer_list]
    outputdata = pd.DataFrame(states_not_guessed)
    outputdata.to_csv("States_not_guessed.csv")