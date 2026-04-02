from turtle import Screen
import Gamelogic


screen = Screen()
screen.setup(width=730,height=500)
screen.title("Name US States Game")
screen.bgpic("blank_states_img.gif")



game_is_on = True
score = 0
answer_list = []

while game_is_on:

    answer = screen.textinput(f"{score}/50 States Correct","Whats another state name?").title()

    if answer == "Exit":
        game_is_on = False
        Gamelogic.game_over(answer_list)
        break

    if answer not in answer_list:
        answer_list.append(answer)
        if Gamelogic.check_answer(answer):
            score += 1
            Gamelogic.state_name_show(answer)

    if score == 50:
        game_is_on = False




