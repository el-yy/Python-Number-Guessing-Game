import tkinter as tk
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.MAX_ATTEMPTS = 5
        self.number = random.randint(1, 100)
        self.attempts = 0

        # Create GUI components
        self.label = tk.Label(root, text="Guess the number between 1 and 100:", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(root, text="Submit", font=("Arial", 14), command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.play_again_button = tk.Button(root, text="Play Again", font=("Arial", 14), command=self.reset_game)
        self.play_again_button.pack(pady=10)
        self.play_again_button.config(state="disabled")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.", fg="red")
            return

        self.attempts += 1

        if guess == self.number:
            self.result_label.config(text=f"Congratulations! You guessed it in {self.attempts} attempts.", fg="green")
            self.end_game()
        elif guess < self.number:
            self.result_label.config(text="Too low! Try again.", fg="blue")
        else:
            self.result_label.config(text="Too high! Try again.", fg="blue")

        if self.attempts >= self.MAX_ATTEMPTS and guess != self.number:
            self.result_label.config(text=f"Game Over! The number was {self.number}.", fg="red")
            self.end_game()

    def end_game(self):
        self.submit_button.config(state="disabled")
        self.play_again_button.config(state="normal")

    def reset_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.submit_button.config(state="normal")
        self.play_again_button.config(state="disabled")

root = tk.Tk()
game = NumberGuessingGame(root)
root.mainloop()
