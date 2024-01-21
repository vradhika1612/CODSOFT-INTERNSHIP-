import tkinter as tk
import random

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'scissors' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game(user_choice):
    computer_choice = get_computer_choice()

    result_label.config(text=f"Computer's choice: {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    result_label.config(text=result)

    if result == "You win!":
        user_score.set(user_score.get() + 1)
    elif result == "You lose!":
        computer_score.set(computer_score.get() + 1)

    play_again_label.config(text="Do you want to play again? (yes/no):")

    computer_label.config(text=f"Computer's choice: {computer_choice}")

    play_again_button = tk.Button(window, text='Yes', padx=20, pady=20, font=('Arial', 12), command=reset_game)
    play_again_button.grid(row=5, column=0)

    no_button = tk.Button(window, text='No', padx=20, pady=20, font=('Arial', 12), command=window.quit)
    no_button.grid(row=5, column=1)

def reset_game():
    play_again_label.config(text="")
    result_label.config(text="")
    computer_label.config(text="")
    play_again_button.grid_forget()
    no_button.grid_forget()

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors Game")

# Labels
user_label = tk.Label(window, text="Your choice:")
user_label.grid(row=0, column=0)

computer_label = tk.Label(window, text="")
computer_label.grid(row=0, column=2)

result_label = tk.Label(window, text="", font=('Arial', 14))
result_label.grid(row=1, column=1)

play_again_label = tk.Label(window, text="")
play_again_label.grid(row=4, column=0, columnspan=2)

# Score variables
user_score = tk.IntVar()
computer_score = tk.IntVar()

# Score labels
tk.Label(window, text="Your Score:").grid(row=2, column=0)
tk.Label(window, textvariable=user_score).grid(row=2, column=1)

tk.Label(window, text="Computer Score:").grid(row=2, column=2)
tk.Label(window, textvariable=computer_score).grid(row=2, column=3)

# Buttons with text labels
rock_button = tk.Button(window, text='Rock', padx=20, pady=20, font=('Arial', 12), command=lambda: play_game('rock'))
rock_button.grid(row=3, column=0)

paper_button = tk.Button(window, text='Paper', padx=20, pady=20, font=('Arial', 12), command=lambda: play_game('paper'))
paper_button.grid(row=3, column=1)

scissors_button = tk.Button(window, text='Scissors', padx=20, pady=20, font=('Arial', 12), command=lambda: play_game('scissors'))
scissors_button.grid(row=3, column=2)

# Start the GUI event loop
window.mainloop()
