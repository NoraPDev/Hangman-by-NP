import random

words_list = []

for line in open('words.txt', 'r').readlines():
    words_list.append(line.strip())

def play(chosen_word):
    """
    Plays the game
    """
    print(play_word)
    word = "_" * len(play_word)
    word_guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
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