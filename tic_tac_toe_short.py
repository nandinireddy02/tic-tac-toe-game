import tkinter as tk
from tkinter import messagebox

def click(i):
    if buttons[i]["text"] == "":
        buttons[i]["text"] = players[turn[0] % 2]
        turn[0] += 1
        check_winner()

def check_winner():
    combos = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for a, b, c in combos:
        if buttons[a]["text"] == buttons[b]["text"] == buttons[c]["text"] != "":
            messagebox.showinfo("Game Over", f"Player {buttons[a]['text']} wins!")
            reset()
            return
    if all(btn["text"] != "" for btn in buttons):
        messagebox.showinfo("Game Over", "It's a tie!")
        reset()

def reset():
    for btn in buttons:
        btn["text"] = ""
    turn[0] = 0

root = tk.Tk()
root.title("Tic Tac Toe")

players = ["X", "O"]
turn = [0]
buttons = [tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                     command=lambda i=i: click(i)) for i in range(9)]

for i, btn in enumerate(buttons):
    btn.grid(row=i//3, column=i%3)

root.mainloop()
