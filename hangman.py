"""File generated by ChatGPT.
Minor edits made by human hand.
"""

import requests
import random
import tkinter as tk
from tkinter import messagebox


def choose_word():
    try:
        response = requests.get("https://www.randomwordgenerator.com/json/words.json")
        words = response.json()['data']
        return random.choice(words)['word'].lower()
    except Exception as e:
        print(f"Error fetching words: {e}")
        return random.choice(["python", "hangman", "programming", "computer", "game", "code"])


def show_message(title, message):
    messagebox.showinfo(title, message)


def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()


class HangmanGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")

        self.word_to_guess = choose_word()
        self.good_guess = []
        self.bad_guess = []
        self.attempts = 10

        self.create_widgets()

    def create_widgets(self):
        # Word to guess
        self.word_label = tk.Label(self.root, text=self.display_word(), font=("Helvetica", 18))
        self.word_label.pack(pady=10)

        # Incorrect guess
        self.incorrect_label = tk.Label(self.root, text="Incorrect Guesses: ", font=("Helvetica", 12))
        self.incorrect_label.pack()

        # Attempts remaining
        self.attempts_label = tk.Label(self.root, text=f"Attempts left: {self.attempts}", font=("Helvetica", 12))
        self.attempts_label.pack()

        # Instruction
        self.guess_label = tk.Label(self.root, text="Guess a letter:", font=("Helvetica", 12))
        self.guess_label.pack()

        # Guess letter -- input
        self.guess_entry = tk.Entry(self.root, font=("Helvetica", 12))
        self.guess_entry.pack()

        # Button
        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess, font=("Helvetica", 12))
        self.guess_button.pack(pady=10)

    def display_word(self):
        return ' '.join([letter if letter in self.good_guess else '_' for letter in self.word_to_guess])

    def make_guess(self):
        """Check to see if guess was correct, incorrect, or invalid (Error)."""
        guess = self.guess_entry.get().lower()

        # Invalid guess
        if not is_valid_guess(guess):
            messagebox.showinfo("Invalid Input", "Please enter a single letter.")
            return

        # Already guessed
        if self.already_guessed(guess):
            messagebox.showinfo("Duplicate Guess", "You've already guessed that letter. Try again.")
            return

        # Guess -> Correct
        if guess in self.word_to_guess:
            self.good_guess.append(guess)
        # Guess -> Incorrect
        else:
            self.attempts -= 1
            self.bad_guess.append(guess)
            self.incorrect_label.config(text=f"Incorrect Guesses: {', '.join(self.bad_guess)}")

        self.attempts_label.config(text=f"Attempts left: {self.attempts}")

        current_display = self.display_word()
        self.word_label.config(text=current_display)

        # Game won
        if set(self.good_guess) == set(self.word_to_guess):
            show_message("Congratulations", f"You guessed the word: {self.word_to_guess}")
            self.root.destroy()

        # Game lost
        if self.attempts == 0:
            show_message("Game Over", f"Sorry, you ran out of attempts. The word was: {self.word_to_guess}")
            self.root.destroy()

    def already_guessed(self, guess):
        return guess in self.good_guess or guess in self.bad_guess


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")  # Set the window dimensions
    hangman_game = HangmanGameGUI(root)
    root.mainloop()
