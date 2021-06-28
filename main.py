import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
not_guessed_sates = all_states
guessed_states = []

# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
game_is_on = True


while len(guessed_states) < 50:
    answer_state = (screen.textinput(title=f" {len(guessed_states)}/40 Guess the State ", prompt="What is another state's name?")).title()
    if answer_state == 'Exit':
        break
    if answer_state in all_states:

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
        guessed_states.append(answer_state)
        not_guessed_sates.remove(f'{answer_state}')

# states_to_learn.csv
print(not_guessed_sates)
df = pandas.DataFrame(not_guessed_sates)
df.to_csv("states_to_learn.csv")












