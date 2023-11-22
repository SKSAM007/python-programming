from tkinter import *
import random

root = Tk()

root.geometry("400x300")
root.title("Rock Paper Scissor Game")

computer_value = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}


def reset_game():
    b1["state"] = "active"
    b2["state"] = "active"
    b3["state"] = "active"
    b4["state"] = "active"
    l1.config(text="Player 1")
    l2.config(text="VS")
    l3.config(text="Player 2")
    l4.config(text="")


def button_disable():
    b1["state"] = "disable"
    b2["state"] = "disable"
    b3["state"] = "disable"
    b4["state"] = "disable"


def isrock_player1():
    play_game("Rock", "Player 1")


def ispaper_player1():
    play_game("Paper", "Player 1")


def isscissor_player1():
    play_game("Scissor", "Player 1")


def isrock_player2():
    play_game("Rock", "Player 2")


def ispaper_player2():
    play_game("Paper", "Player 2")


def isscissor_player2():
    play_game("Scissor", "Player 2")


def play_game(player_choice, player_label):
    computer_choice = computer_value[str(random.randint(0, 2))]

    if player_choice == computer_choice:
        match_result = "Match Draw"
    elif (
        (player_choice == "Rock" and computer_choice == "Scissor")
        or (player_choice == "Paper" and computer_choice == "Rock")
        or (player_choice == "Scissor" and computer_choice == "Paper")
    ):
        match_result = f"{player_label} Wins"
    else:
        match_result = "Computer Wins"

    l4.config(text=match_result)
    l1.config(text=f"{player_label}: {player_choice}")
    l3.config(text=f"Computer: {computer_choice}")
    button_disable()


Label(root, text="Rock Paper Scissor", font="normal 20 bold", fg="blue").pack(pady=20)

frame = Frame(root)
frame.pack()

l1 = Label(frame, text="Player 1", font=10)
l2 = Label(frame, text="VS", font="normal 10 bold")
l3 = Label(frame, text="Player 2", font=10)

l1.pack(side=LEFT)
l2.pack(side=LEFT)
l3.pack()

l4 = Label(
    root,
    text="",
    font="normal 20 bold",
    bg="white",
    width=15,
    borderwidth=2,
    relief="solid",
)
l4.pack(pady=20)

frame1 = Frame(root)
frame1.pack()

b1 = Button(frame1, text="Rock", font=10, width=7, command=isrock_player1)
b2 = Button(frame1, text="Paper", font=10, width=7, command=ispaper_player1)
b3 = Button(frame1, text="Scissor", font=10, width=7, command=isscissor_player1)

b1.pack(side=LEFT, padx=10)
b2.pack(side=LEFT, padx=10)
b3.pack(padx=10)

frame2 = Frame(root)
frame2.pack()

b4 = Button(frame2, text="Rock", font=10, width=7, command=isrock_player2)
b5 = Button(frame2, text="Paper", font=10, width=7, command=ispaper_player2)
b6 = Button(frame2, text="Scissor", font=10, width=7, command=isscissor_player2)

b4.pack(side=LEFT, padx=10)
b5.pack(side=LEFT, padx=10)
b6.pack(padx=10)

Button(root, text="Reset Game", font=10, fg="red", bg="black", command=reset_game).pack(
    pady=20
)

# Execute Tkinter
root.mainloop()
