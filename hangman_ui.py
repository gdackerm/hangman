import tkinter as tk
import random

class HangmanUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        self.word_list = ["python", "hangman", "challenge", "interface", "random"]
        self.word_to_guess = random.choice(self.word_list)
        self.guessed_letters = []
        self.remaining_guesses = 6
        
        self.create_widgets()
        self.update_display()
        
    def create_widgets(self):
        self.word_display = tk.Label(self.master, text="", font=("Helvetica", 18))
        self.word_display.pack(pady=10)
        
        self.incorrect_guesses_display = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.incorrect_guesses_display.pack(pady=10)
        
        self.remaining_guesses_display = tk.Label(self.master, text=f"Remaining guesses: {self.remaining_guesses}", font=("Helvetica", 14))
        self.remaining_guesses_display.pack(pady=10)
        
        self.hangman_graphic = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.hangman_graphic.pack(pady=10)
        
        self.guess_entry = tk.Entry(self.master, font=("Helvetica", 14))
        self.guess_entry.pack(pady=10)
        
        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.process_guess, font=("Helvetica", 14))
        self.submit_button.pack(pady=10)
        
        self.message_display = tk.Label(self.master, text="", font=("Helvetica", 14))
        self.message_display.pack(pady=10)
        
    def update_display(self):
        display_word = " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word_to_guess])
        self.word_display.config(text=display_word)
        
        incorrect_guesses = " ".join([letter for letter in self.guessed_letters if letter not in self.word_to_guess])
        self.incorrect_guesses_display.config(text=f"Incorrect guesses: {incorrect_guesses}")
        
        self.remaining_guesses_display.config(text=f"Remaining guesses: {self.remaining_guesses}")
        
        hangman_stages = [
            "",
            "O",
            "O\n|",
            "O\n/|",
            "O\n/|\\",
            "O\n/|\\\n/",
            "O\n/|\\\n/ \\"
        ]
        self.hangman_graphic.config(text=hangman_stages[6 - self.remaining_guesses])
        
    def process_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)
        
        if guess in self.guessed_letters:
            self.message_display.config(text="You already guessed that letter.")
            return
        
        self.guessed_letters.append(guess)
        
        if guess not in self.word_to_guess:
            self.remaining_guesses -= 1
        
        self.update_display()
        self.check_game_status()
        
    def check_game_status(self):
        if all(letter in self.guessed_letters for letter in self.word_to_guess):
            self.message_display.config(text="Congratulations! You won!")
            self.submit_button.config(state=tk.DISABLED)
        elif self.remaining_guesses == 0:
            self.message_display.config(text=f"Game Over! The word was '{self.word_to_guess}'.")
            self.submit_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    hangman_ui = HangmanUI(root)
    root.mainloop()
