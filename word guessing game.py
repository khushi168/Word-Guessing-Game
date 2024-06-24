import random
import pandas as pd
from collections import Counter

# place the csv file path here
df = pd.read_csv('C:/Users/HP/Downloads/words_dataset.csv')

# Extract the words from the 'word' column of the dataset
words_list = df['WORD'].tolist()

# Randomly choose a secret word from the dataset
word = random.choice(words_list).lower()  # Convert the word to lowercase


def set_difficulty():
    while True:
        try:
            difficulty = int(input("Choose the difficulty level (1: Easy, 2: Medium, 3: Hard): "))
            if 1 <= difficulty <= 3:
                return difficulty
            else:
                print("Invalid input. Please choose a difficulty level between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def reveal_hints(word):
    # Randomly choose two indices in the word to reveal
    word_length = len(word)
    hint_indices = random.sample(range(word_length), min(2, word_length))

    # Create a list to store the word with hints revealed
    revealed_word = list('_' * word_length)

    # Reveal the letters at the chosen indices
    for index in hint_indices:
        revealed_word[index] = word[index]

    return ' '.join(revealed_word)


if __name__ == '__main__':
    print('Guess the word!')
    difficulty = set_difficulty()
    max_chances = 11 - difficulty * 3

    # Reveal hints before the player starts guessing
    print("Word to guess:", reveal_hints(word))

    playing = True
    # list for storing the letters guessed by the player
    letterGuessed = ''
    chances = max_chances
    correct = 0
    flag = 0
    try:
        while chances != 0 and flag == 0:  # flag is updated when the word is correctly guessed
            print()
            chances -= 1

            try:
                guess = str(input('Enter a letter to guess: ')).lower()  # Convert user input to lowercase
            except:
                print('Enter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('You have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word:
                # k stores the number of times the guessed letter occurs in the word
                k = word.count(guess)
                for _ in range(k):
                    letterGuessed += guess  # The guess letter is added as many times as it occurs
                chances += 1  # Increment chances for correct guess

            # Print the word
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters
                # Once the correct word is guessed fully,
                elif Counter(letterGuessed) == Counter(word):
                    # the game ends, even if chances remain
                    print("The word is:", end=' ')
                    print(word)
                    flag = 1
                    print('Congratulations, You won!')
                    break  # To break out of the for loop
                else:
                    print('_', end=' ')

        # If user has used all of his chances
        if chances == 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('You lost! Try again..')
            print('The word was {}'.format(word))

    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()
