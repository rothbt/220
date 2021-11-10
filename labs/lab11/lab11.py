"""
Name: Benjamin Roth
lab11.py
"""

from random import randint


def word_pool():
    file = open("wordslist.txt")
    pool = []
    for line in file:
        word = line
        pool.append(word.strip())
    return pool


def secret_word(pool):
    random_word = pool[randint(0, len(pool) - 1)]
    return random_word


def guessWord(secret_word, guessed_letters, guessed_word, letter):
    check = False
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            guessed_word[i] = letter
            check = True
    if check == True:
        return True
    guessed_letters.append(letter)
    return False


def guessedLetters(guessed_letters, secret_word, guessed_word):
    letter = input("Guess a letter: ")
    letter = letter.lower()
    check = False
    while check == False:
        check = True
        for ch in guessed_letters:
            if letter == ch:
                print("That letter has already been guessed, guess again: ")
                letter = input("Guess a letter: ")
                letter = letter.lower()
                check = False
    if guessWord(secret_word, guessed_letters, guessed_word, letter):
        return True
    else:
        return False


def print_table(guessed_word, turn_count, guessed_letters):
    print(guessed_word)
    print("Turn count: ", turn_count)
    print("Guessed letters: ", guessed_letters)


def is_won(guessed_word, secret_word):
    if "".join(guessed_word) == secret_word:
        return True
    else:
        return False


def play_game():
    turn_count = 0
    s_word = secret_word(word_pool())
    g_word = []
    for _ in range(len(s_word) - 1):
        g_word.append("_")
    guessed_letters = []
    print_table(g_word, turn_count, guessed_letters)

    while turn_count < 7 and not is_won(g_word, s_word):
        if guessedLetters(guessed_letters, s_word, g_word) == False:
            turn_count += 1
            print_table(g_word, turn_count, guessed_letters)
        print_table(g_word, turn_count, guessed_letters)
    if turn_count >= 7:
        print("you lose")
    elif is_won(g_word, s_word):
        print("congats")







def main():
    play_game()
    pass


if __name__ == '__main__':
    main()
