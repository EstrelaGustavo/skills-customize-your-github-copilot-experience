
# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a playable Hangman game in Python. Practice using strings, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Choose a hidden word from the provided list and initialize the variables needed to track the player's guesses and remaining attempts.

#### Requirements
Completed program should:

- Randomly select one word from the provided `words` list.
- Set up a collection to track guessed letters.
- Set and track the maximum number of incorrect guesses allowed.


### 🛠️ Run the Guessing Game

#### Description
Let the player guess letters until they reveal the word or run out of incorrect guesses. Show the word's progress after each guess.

#### Requirements
Completed program should:

- Prompt the player to enter a letter on each turn.
- Display each letter in the word when guessed, and use an underscore for each letter not yet guessed (for example, `_ _ _`).
- Track incorrect guesses and show how many attempts remain.
- End when the player guesses the full word or reaches the maximum number of incorrect guesses.
- Display a clear win or lose message. If the player loses, reveal the hidden word.
