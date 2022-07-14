import random
import sys
from os import system, name


class text_colors:
    """
    Defines terminal text color
    """
    MAGENTA = '\u001b[35m'
    BLUE = '\u001b[34m'
    WHITE = '\u001b[37m'

words_list = []

for line in open('words.txt', 'r').readlines():
    words_list.append(line.strip())


def play(play_word, lives):
    """
    Plays the game
    """
    word = "_" * len(play_word)
    word_guessed = False
    guessed_letters = []
    tries = lives
    print("Let's play Hangman!")
    print("\n")
    while not word_guessed and tries > 0:
        print(guessed_letters)
        print(word)
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess not in play_word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                display_hangman(tries)
            elif guess in guessed_letters:
                print("You already guessed this letter.")
            else:
                print(f"Well done, {guess} is in the word! Easy-peasy!")
                guessed_letters.append(guess)
                display_hangman(tries)

                word_template_list = list(word)
                indices = [
                    i for i, letter in enumerate(play_word) if letter == guess]
                for index in indices:
                    word_template_list[index] = guess
                    word = "".join(word_template_list)
                    if "_" not in word:
                        word_guessed = True
        else:
            print("Please only enter a single letter!")
    if word_guessed:
        correct_word()
        print("You WON! Well Done! :)")
        end_game(play_word)
    else:
        display_hangman(0)
        incorrect_word()
        print("your guess was wrong!")
        print(f"the word was {play_word}")
        end_game(play_word)


def initialise_game():
    """
    Sets up game, select difficulty level
    """
    play_word = random.choice(words_list).upper()
    hangman_initial()

    while True:
        print('Welcome to Hangman By Nora!\nYou can choose difficulty level [E]asy, [M]edium or [H]ard')
        difficulty = input('Please choose now: ')
        # Input to select difficulty#
        if difficulty.lower() == 'e':
            play(play_word, 6)
        elif difficulty.lower() == 'm':
            play(play_word, 4)
        elif difficulty.lower() == 'h':
            play(play_word, 2)
        else:
            print('Please go back and choose a level!')


def end_game(word):
    """
    Ends game
    """
    while True:
        response = input("Do you want to play again [y]es or [n]o")
        if response.lower() == 'y':
            print('You are about to start a new game!')
            initialise_game()
            break
        elif response.lower() == 'n':
            print('See you later, alligator!')
            sys.exit()


def hangman_initial():
    """
    Graphic Hangman logo.
    """
    print(
        """
        ░░   ░░  ░░░░░  ░░░    ░░  ░░░░░░  ░░░    ░░░  ░░░░░  ░░░    ░░
        ▒▒   ▒▒ ▒▒   ▒▒ ▒▒▒▒   ▒▒ ▒▒       ▒▒▒▒  ▒▒▒▒ ▒▒   ▒▒ ▒▒▒▒   ▒▒
        ▒▒▒▒▒▒▒ ▒▒▒▒▒▒▒ ▒▒ ▒▒  ▒▒ ▒▒   ▒▒▒ ▒▒ ▒▒▒▒ ▒▒ ▒▒▒▒▒▒▒ ▒▒ ▒▒  ▒▒
        ▓▓   ▓▓ ▓▓   ▓▓ ▓▓  ▓▓ ▓▓ ▓▓    ▓▓ ▓▓  ▓▓  ▓▓ ▓▓   ▓▓ ▓▓  ▓▓ ▓▓
        ██   ██ ██   ██ ██   ████  ██████  ██      ██ ██   ██ ██   ████
        """
    )


def display_hangman(lives):
    """
    Displays hangman graphic based on lives left
    """
    lives_left = [
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        / \\
        |\\
        ========
        """,
        """
        ___________
        |/        |
        |         O
        |        /|\\
        |         |
        |        /
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|\\
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |        /|
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |         |
        |         |
        |
        |\\
        ========
        """,
        """
        __________
        |/        |
        |         O
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |\\
        ========
        """,
        """
        __________
        |/
        |
        |
        |
        |
        |
        ========
        """,
        """
        |/
        |
        |
        |
        |
        |
        ========
        """,

        """
        |
        |
        |
        |
        |
        ========
        """,
        """
        """
    ]
    print(lives_left[lives])


def correct_word():
    """
    When player guessed the word correctly, this will go on display
    """
    print(
        text_colors.MAGENTA + """
        __   __
        \\ \\ / /__  _   _
         \\ V / _ \\| | | |
          | | (_) | |_| |
          |_|\\___/_\\__,_| _
        __      _(_)_ __ | |
        \\ \\ /\\ / / | '_ \\| |
         \\ V  V /| | | | |_|
          \\_/\\_/ |_|_| |_(_)
        """ + text_colors.WHITE
        )


def incorrect_word():
    """
    Word guessed incorrectly, displays below
    """
    print(
        text_colors.BLUE + """
          ____
         / ___| __ _ _ __ ___   ___
        | |  _ / _` | '_ ` _ \\ / _ \\
        | |_| | (_| | | | | | |  __/
         \\____|\\__,_|_| |_| |_|\\___|
         / _ \\__   _____ _ __| |
        | | | \\ \\ / / _ \\ '__| |
        | |_| |\\ V /  __/ |  |_|
         \\___/  \\_/ \\___|_|  (_)
        """ + text_colors.WHITE
        )


def main():
    initialise_game()

main()