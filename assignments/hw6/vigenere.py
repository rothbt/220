"""
Name: Benjamin Roth
vigenere.py

Problem: this program will encode a message using a vigenere cipher

Certification of Authenticity:
I verify that this assignment is entirely my own work.
"""

from graphics import GraphWin, Point, Rectangle, Text, Entry
import string

# write function code that accepts (message, and keyword) and returns the encoded message


def code(message, keyword):

    alphabet = string.ascii_uppercase

    # index both inputs
    # why does it append each character and not each word in list?
    split_message = message.split()
    indexed_message = []
    for word in split_message:
        upper_message = word.upper()
        indexed_message += upper_message

    split_key = keyword.split()
    indexed_key = []
    for k_word in split_key:
        upper_key = k_word.upper()
        indexed_key += upper_key

    vig_message = []
    for chr in indexed_message:
        vig = alphabet.find(chr)
        vig_message.append(vig)

    vig_key = []
    for i in range(len(indexed_message)):
        ordinal = alphabet.find(indexed_key[i % len(indexed_key)])
        vig_key.append(ordinal)

    # encode using vigenere cipher
    encoded = []
    for i in range(len(vig_message)):
        encoded_chr = int(vig_key[i]) + int(vig_message[i])
        vig_fix = encoded_chr % len(alphabet)
        encoded.append(vig_fix)

    # return ciphered values to english characters
    decoded = ''
    for num in encoded:
        e_chr = alphabet[num]
        decoded += e_chr

    return decoded


def main():
    # create a graphics window
    win = GraphWin("Vigenere", 600, 600, autoflush=False)
    win.setCoords(0, 0, 6, 6)

    # design graphics interface
    workspace = Rectangle(Point(.25, .25), Point(5.75, 5.75))
    workspace.setFill("white")

    message_text = Text(Point(2, 4), "What is the message?:")
    key_text = Text(Point(2, 3.5), "        What is the key?:")
    message_text.setSize(15)
    key_text.setSize(15)

    input_message = Entry(Point(3.85, 4), 25)
    input_key = Entry(Point(3.5, 3.5), 15)

    button = Rectangle(Point(2, 3), Point(4, 2))
    button_text = Text(Point(3, 2.5), "Encode!")

    # draw input interface

    workspace.draw(win)
    message_text.draw(win)
    key_text.draw(win)
    input_message.draw(win)
    input_key.draw(win)
    button.draw(win)
    button_text.draw(win)
    win.update()

    win.getMouse()

    # gather inputs for message and keyword
    message = input_message.getText()
    keyword = input_key.getText()

    # undraw button
    button.undraw()
    button_text.undraw()

    # display encoded messsage
    display = Text(Point(3, 2.5), "Your encoded message is:")
    encoded = code(message, keyword)
    encoded_disp = Text(Point(3, 2), encoded)
    encoded_disp.setSize(15)
    display.draw(win)
    encoded_disp.draw(win)

    # click to close
    close_text = Text(Point(3, 1), "Click to Close!")
    close_text.draw(win)
    win.update()

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
