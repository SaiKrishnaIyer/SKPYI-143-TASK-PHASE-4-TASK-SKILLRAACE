from tkinter import *
from tkinter import messagebox
import random

def ButtonClick(button):
    global x_o, flag
    if button["text"] == "" and x_o:
        button["text"] = "X"
        x_o = False
        flag += 1
        checkforwin()
        if not x_o:  # If it's the computer's turn
            computer_move()
            checkforwin()

def computer_move():
    global x_o, flag
    available_buttons = [button for button in buttons if button["text"] == ""]
    if available_buttons:
        button = random.choice(available_buttons)
        button["text"] = "O"
        button["bg"] = "#2ec4b6"
        x_o = True
        flag += 1

def checkforwin():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    winning_combinations = [
        (button1, button2, button3),
        (button4, button5, button6),
        (button7, button8, button9),
        (button1, button5, button9),
        (button3, button5, button7),
        (button1, button4, button7),
        (button2, button5, button8),
        (button3, button6, button9),
    ]
    for combo in winning_combinations:
        if combo[0]["text"] == combo[1]["text"] == combo[2]["text"] != "":
            messagebox.showinfo("Tic Tac Toe", f"Player {combo[0]['text']} won!")
            reset_game()
            return
    if flag == 9:
        messagebox.showinfo("Tic Tac Toe", "Game Tied!")
        reset_game()

def reset_game():
    global x_o, flag
    x_o = True
    flag = 0
    for button in buttons:
        button["text"] = ""
        button["bg"] = "#ffb5a7"

main = Tk()
main.title("Tic Tac Toe")

x_o = True
flag = 0

buttons = []

button1 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: ButtonClick(button1))
button1.grid(row=0, column=0)
buttons.append(button1)
button2 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: ButtonClick(button2))
button2.grid(row=0, column=1)
buttons.append(button2)
button3 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: ButtonClick(button3))
button3.grid(row=0, column=2)
buttons.append(button3)
button4 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: ButtonClick(button4))
button4.grid(row=1, column=0)
buttons.append(button4)
button5 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: ButtonClick(button5))
button5.grid(row=1, column=1)
buttons.append(button5)
button6 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: ButtonClick(button6))
button6.grid(row=1, column=2)
buttons.append(button6)
button7 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: ButtonClick(button7))
button7.grid(row=2, column=0)
buttons.append(button7)
button8 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: ButtonClick(button8))
button8.grid(row=2, column=1)
buttons.append(button8)
button9 = Button(main, text="", font=("arial", 60, "bold"), bg="#ffb5a7", fg="white", width=3, command=lambda: ButtonClick(button9))
button9.grid(row=2, column=2)
buttons.append(button9)

main.mainloop()
