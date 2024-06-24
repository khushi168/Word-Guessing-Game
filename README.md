# Word Guessing Game

This Word Guessing Game is a fun, Python-based game where players try to guess a randomly chosen word from a custom dataset. The game features three difficulty levels (Easy, Medium, and Hard), each with a different number of guesses. Players earn an extra guess for each correct letter they guess.

## Features

- **Three Difficulty Levels**: Easy, Medium, and Hard.
- **Hints**: Two letters of the word are revealed as hints before the guessing starts.
- **Dynamic Guessing**: Players earn extra guesses for each correct letter guessed.
- **Interactive Gameplay**: The game interacts with the player through the console, providing feedback on each guess.

## Dataset

The dataset is a CSV file containing a list of words. This file should be placed in the directory specified in the code.

## Requirements

- Python 3.x
- pandas

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/word-guessing-game.git
    ```

2. **Navigate to the Project Directory**:
    ```sh
    cd word-guessing-game
    ```

3. **Install Dependencies**:
    ```sh
    pip install pandas
    ```

4. **Prepare the Dataset**:
    - Ensure your dataset CSV file (`words_dataset.csv`) is placed in the correct path as specified in the code.

## Usage

1. **Run the Game**:
    ```sh
    python word_guessing_game.py
    ```

2. **Gameplay**:
    - Choose a difficulty level (1: Easy, 2: Medium, 3: Hard).
    - Start guessing letters to figure out the word.
    - You will see hints (two revealed letters) before you start guessing.
    - Earn extra guesses for each correct letter.
    - Win by guessing all the letters in the word within the allowed number of guesses.

## Code Explanation

The game is structured as follows:

1. **Dataset Loading**:
    - The dataset is loaded from a CSV file using pandas.
    - A random word is selected from the dataset.

2. **Setting Difficulty**:
    - The player selects a difficulty level, which determines the number of initial guesses.

3. **Revealing Hints**:
    - Two random letters in the word are revealed to help the player.

4. **Main Game Loop**:
    - The player guesses letters until they either guess the word correctly or run out of guesses.
    - Correct guesses earn extra chances.
    - The game provides feedback on each guess and ends when the word is guessed or guesses are exhausted.

5. **End Game**:
    - The game congratulates the player on winning or informs them of the correct word if they lose.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue to suggest improvements or report bugs.

## License

This project is licensed under the MIT License.
