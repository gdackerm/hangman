# hangman
Copilot workspace kicking the tires

## Goal
The goal of this project is to create a simple game of hangman using Copilot workspace.

## How to Run the Game
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the game using the command: `python hangman.py`
4. To run the game with the user interface, use the command: `python hangman_ui.py`

## Game Rules
1. The game will randomly select a word.
2. The player will try to guess the word by suggesting letters within a certain number of guesses.
3. If the player suggests a letter that is in the word, the letter appears in the correct position(s).
4. If the player suggests a letter that is not in the word, the number of remaining guesses decreases.
5. The game ends when the player guesses the word correctly or runs out of guesses.

## User Interface
The user interface includes the following elements:
* A display area for the word to be guessed, with underscores representing unguessed letters
* A display area for the letters that have been guessed incorrectly
* A display area for the number of remaining guesses
* A display area for the hangman graphic, which updates as incorrect guesses are made
* An input field for the player to enter their guesses
* A button to submit the guess
* A message area to display game status (e.g., win/lose messages)
