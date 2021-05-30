from tkinter import *
import random

def next_turn(row , column):
    global player
    if buttons[row][column]['text'] == "" and check_winner(buttons) is False:       
        if player == players[0]:          
            buttons[row][column]['text'] = player
            if check_winner(buttons) is False:
                player = players[1]
                lb.config(text=(players[1]+" turn"))
            elif check_winner(buttons) is True:
                lb.config(text = (players[0]+ " win"))
            elif check_winner(buttons) == "Tie":
                lb.config(text = ("Tie"))
        else:
            buttons[row][column]['text'] = player
            if check_winner(buttons) is False:
                player = players[0]
                lb.config(text=(players[0]+" turn"))
            elif check_winner(buttons) is True:
                lb.config(text = (players[1]+ " win"))
            elif check_winner(buttons) == "Tie":
                lb.config(text = ("Tie!"))
def check_winner(broad):
    for row in range(3):
        if broad[row][0]['text'] == broad[row][1]['text'] == broad[row][2]['text'] != "":
            broad[row][0].config(bg = "#5efc03")
            broad[row][1].config(bg = "#5efc03")
            broad[row][2].config(bg = "#5efc03")
            return True
    for column in range(3):
        if broad[0][column]['text'] == broad[1][column]['text'] == broad[2][column]['text'] != "":
            broad[0][column].config(bg = "#5efc03")
            broad[1][column].config(bg = "#5efc03")
            broad[2][column].config(bg = "#5efc03")
            return True
    if broad[0][0]['text'] == broad[1][1]['text'] == broad[2][2]['text'] != "":
        broad[0][0].config(bg = "#5efc03")
        broad[1][1].config(bg = "#5efc03")
        broad[2][2].config(bg = "#5efc03")
        return True
    elif broad[0][2]['text'] == broad[1][1]['text'] == broad[2][0]['text'] != "":
        broad[0][2].config(bg = "#5efc03")
        broad[1][1].config(bg = "#5efc03")
        broad[2][0].config(bg = "#5efc03")
        return True
    elif empty_spaces() is False:
        for row in range(3):
            for column in range(3):
                broad[row][column].config(bg = "#e5eb34")
        return "Tie"
    else:
        return False
def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True 
                break
    return False

def new_game():
    global player

    player = random.choice(players)

    lb.config(text= player + " turn")
    
    for row in range(3):
        for column in range(3):
            buttons[row][column]['text'] = ""
            buttons[row][column].config(bg =orig_color)

win = Tk()
win.title("Tic Tac Toe")

win_width = 500
win_height = 500
screen_width = win.winfo_screenwidth()
screen_height = win.winfo_screenheight()

x =int ((screen_width / 2 ) - (win_width / 2))
y =int ((screen_height / 2 ) - (win_height / 2))
win.geometry("{}x{}+{}+{}".format(win_width,win_height, x ,y))


players = ["X","O"]
player = random.choice(players)
buttons = [[0,0,0],[0,0,0],[0,0,0]]

lb = Label(text = player + " turn", font = ('consolas',40))
lb.pack(side="top")

btn_reset = Button(text = "Restart", font=('consolas',20), command=new_game)
btn_reset.pack(side="top")

orig_color = btn_reset.cget("background")

frame = Frame(win)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text ="",font = ('consolas',28), width=5, height=2, command= lambda row = row, column = column :next_turn(row,column))
        buttons[row][column].grid(row = row, column =column)
win.mainloop()