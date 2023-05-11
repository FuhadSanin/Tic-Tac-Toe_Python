from tkinter import *
import random


def reset_game():
    global player

    player = random.choice(players)
    label.config(text=player + " Players", fg='black')
    for i in range(3):
        for j in range(3):
            button[i][j].config(text="", fg='black')


def check_winner():
    for r in range(3):
        if button[r][0]['text'] == button[r][1]['text'] == button[r][2]['text'] != "":
            button[r][0].config(fg='green', bg='green')
            button[r][1].config(fg='green')
            button[r][2].config(fg='green')
            return True

    for c in range(3):
        if button[0][c]['text'] == button[1][c]['text'] == button[2][c]['text'] != "":
            button[0][c].config(fg='green')
            button[1][c].config(fg='green')
            button[2][c].config(fg='green')
            return True

    if button[0][0]['text'] == button[1][1]['text'] == button[2][2]['text'] != "":
        button[0][0].config(fg='green')
        button[1][1].config(fg='green')
        button[2][2].config(fg='green')
        return True

    elif button[0][2]['text'] == button[1][1]['text'] == button[2][0]['text'] != "":
        button[0][2].config(fg='green')
        button[1][1].config(fg='green')
        button[2][0].config(fg='green')
        return True

    elif empty_spaces() is False:
        for i in range(3):
            for j in range(3):
                button[i][j].config(fg='orange', bg='yellow')
        return "Tie"
    else:
        return False


def next_turn(row, col):
    # global is used to access the global variable
    global player

    # ['text'] is used to get the text of the button
    if button[row][col]['text'] == "" and check_winner() is False:
        if player == players[0]:
            button[row][col]['text'] = player
            # check for winner in 3 cases
            if check_winner() is False:
                player = players[1]
                label.config(text=player + " Player")
            elif check_winner() is True:
                player = players[0]
                label.config(text=player + " Wins", fg='green')
            elif check_winner() == "Tie":
                label.config(text="Tie Game", fg='orange')

        else:
            button[row][col]['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=player + " Player")
            elif check_winner() is True:
                player = players[1]
                label.config(text=player + " Wins", fg='green')
            elif check_winner() == "Tie":
                label.config(text="Tie Game" ,fg='orange')


def empty_spaces():
    spaces = 9
    for i in range(3):
        for j in range(3):
            if button[i][j]['text'] != "":
                spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


window = Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
button = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

label = Label(text=player + " turn", font=('consolas', 40))
label.pack(side="top")

reset_button = Button(text="Restart", font=('consolas', 20), command=reset_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()
frame.config(bg='white')

for row in range(3):
    for column in range(3):
        button[row][column] = Button(frame, text="", font=('consolas', 40), bg='gray', width=5, height=3,
                                     command=lambda r=row, c=column: next_turn(r, c))
        button[row][column].grid(row=row, column=column)

window.mainloop()
