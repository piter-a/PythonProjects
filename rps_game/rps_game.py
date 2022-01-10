from tkinter import *
import random

# initialize a window using the tinkter module
root = Tk()
root.geometry('400x400')
root.resizable(0, 0)
root.title("Rock-Paper-Scissors game")
root.config(bg='lightblue')

# set the heading of the window
Label(root, text='Rock-Paper-Scissors',
      font='arial 20 bold', bg='lightblue').pack()

# user_input variable
# create a label containing name of the game
# create entry box in which user enters their choice
user_input = StringVar()
Label(root, text='Choose one: --Rock,Paper,Scissors--',
      font='arial 15 bold', bg='lightblue').place(x=20, y=70)
Entry(root, font='arial 15', textvariable=user_input,
      bg='green').place(x=90, y=130)

# variables used to store results for each round, current score, and number of rounds computer and user won
result = StringVar()
current_score = StringVar()
pwins = IntVar()
cwins = IntVar()

# this function handles the logic behind the game


def play():
    options = ['rock', 'paper', 'scissors']
    comp_choice = random.choice(options)
    user = user_input.get()

    if user != 'rock' and user != 'paper' and user != 'scissors':
        result.set('Invalid input, select rock, paper, or scissors.')

    elif user == comp_choice:
        result.set(
            f"It's a tie, computer also selected {comp_choice}. Play again.")

    elif user == 'rock' and comp_choice == 'scissors':
    	pwins.set(pwins.get() + 1)
    	result.set(
        	f'You win this round, computer selected {comp_choice}. Play again.')

    elif user == 'paper' and comp_choice == 'rock':
    	pwins.set(pwins.get() + 1)
    	result.set(
        	f'You win this round, computer selected {comp_choice}. Play again.')

    elif user == 'scissors' and comp_choice == 'paper':
    	pwins.set(pwins.get() + 1)
    	result.set(
        	f'You win this round, computer selected {comp_choice}. Play again')

    else:
    	cwins.set(cwins.get() + 1)
    	result.set(
        	f'Computer wins this round, computer selected {comp_choice}. Play again')

# this function resets everything to start state


def Reset():
    result.set("")
    user_input.set("")
    current_score.set("")
    pwins.set(0)
    cwins.set(0)

# this function exits the game


def Exit():
    root.destroy()

# this function is used to clear the user input box


def clear_text():
    user_input.set("")

# this function prints current score and final score


def print_score():
    current_score.set(
        f"Current Score --- Player Score: {pwins.get()}, Computer Score {cwins.get()}")

    if pwins.get() == 3:
        result.set('Congrats, you won! Reset to play again or exit.')

    elif cwins.get() == 3:
        result.set('Sorry, you lost. Reset to play again or exit.')


# buttons and box displaying the score
Entry(root, font='arial 10 bold', textvariable=result,
      bg='green', width=50).place(x=25, y=250)
Entry(root, font='arial 10 bold', textvariable=current_score,
      bg='green', width=50).place(x=25, y=280)
Button(root, font='arial 13 bold', text='PLAY', padx=5, bg='lightblue',
       command=lambda: [play(), clear_text(), print_score()]).place(x=150, y=190)
Button(root, font='arial 13 bold', text='RESET', padx=5,
       bg='lightblue', command=Reset).place(x=70, y=310)
Button(root, font='arial 13 bold', text='EXIT', padx=5,
       bg='lightblue', command=Exit).place(x=230, y=310)

root.mainloop()
