import random

words_list = []

for line in open('words.txt', 'r').readlines():
    words_list.append(line.strip())

def play(chosen_word, lives):
    """
    Plays the game
    """
    print(play_word)
    word = "_" * len(play_word)
    word_guessed = False
    guessed_letters = []
    guessed_words = []
    tries = lives
    print("Let's play Hangman!")
    print(word)
    print("\n")
    while not word_guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess not in play_word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            elif guess in guessed_letters:
                print("You already guessed this letter.")
            else:
                print(f"Well done, {guess} is in the word! Easy-peasy!")
                guessed_letters.append(guess)

                word_template_list = list(word)
                indices = [i for i, letter in enumerate(play_word)
                            if letter == guess]
                for index in indices:
                    word_template_list[index] = guess
                    word = "".join(word_template_list)
                    if "_" not in word:
                        word_guessed = True

    print(display_hangman(tries))
    end_game(play_word)

def initialise_game():
    """
    Sets up game
    """
    chosen_word = random.choice(words_list).upper()
    play(chosen_word, 6)

    while True:
        print('Choose [E]asy, [M]edium or [H]ard')
        difficulty = input('Please choose!')
        #Input to select difficulty#
        if difficulty.lower() == 'e':
            play(chosen_word, 6)
        elif difficulty.lower() == 'm':
            play(chosen_word, 4)
        elif difficulty.lower() == 'h':
            play(chosen_word, 2)
        else:
            print('Please go back and choose a level!')

def end_game(word):
    """
    Ends game
    """
    print("Your guess was wrong!")
    print(f"The word was {word}")

    while True:
        response = input("Do you want to play again [y]es or [n]o")
        if response.lower() == 'y':
            print('you want to play again')
            initialise_game()
            break
        elif response.lower() == 'n':
            print('You dont wanna')
            break

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
​
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
    return lives_left[lives]


initialise_game()