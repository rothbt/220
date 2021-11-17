"""
Name: Benjamin Roth
lab12.py
"""

from random import randint


def find_and_remove_first(n_list, value):
    try:
        i = n_list.index(value)
        name = input("What is the your name")
        n_list[i] = name
    except:
        pass


def read_data(filename):
    file = open(filename, "r")
    line = file.readline()
    line_split = line.split()
    i = 0
    while i < len(line_split):
        line_split[i] = int(line_split[i])
    return line_split


def is_in_linear(search_value, value_list):
    i = 0
    while i < len(value_list):
        if value_list[i] == search_value:
            return True
        i += 1
    return False


def good_input():
    user_input = eval(input("Enter a number between 1 & 10"))
    while not 0 < user_input < 10:
        user_input = eval(input("Enter a number between 1 & 10, headass"))

    return user_input


def num_digits():
    number = eval(input("Enter a positive number"))
    while number > 0:
        i = 0
        while number > 0:
            number //= 10
            i += 1
        print("the # of digits is", i)
        number = eval(input('Enter a positive number, headass'))


def hi_lo_game():
    secret_number = randint(0, 100)
    user_input = eval(input("Guess a number between 0 and 100"))
    guesses = 0
    while user_input != secret_number and guesses <= 7:
        if user_input > secret_number:
            print("The number is too high, guess again!")
            user_input = eval(input("Guess a number between 0 and 100"))
        elif user_input < secret_number:
            print("The number is too low, guess again!")
            user_input = eval(input("Guess a number between 0 and 100"))
        guesses += 1
    if user_input == secret_number:
        print("Congrats you won in", guesses, "guesses")
    else:
        print("sorry you lost, the correct # is", secret_number)


def main():
    # find_and_remove_first()
    # is_in_linear(search_value, read_data("dataSorted.txt"))
    # good_input()
    # num_digits()
    # hi_lo_game()
    pass


main()
