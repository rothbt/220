"""
Name: Benjamin Roth
lab8.py
"""
from lab7 import encode, encode_better

def number_words(infile_name, outfile_name):
    infile = open(infile_name, "r")
    outfile = open(outfile_name,"w")

    for line in infile:
        new_line = line.split()
        i = 1
        for word in new_line:
            outfile.write(str(i) + " " + word + '\n')
            i += 1

    infile.close()
    outfile.close()

def hourly_wages(infile_name, outfile_name):
    infile = open(infile_name, "r")
    outfile = open(outfile_name, "w")

    for line in infile:
        new_line = line.split()
        new_line[2] = str(float(new_line[2]) + 1.65)
        outfile.write(" ".join(new_line) + '\n')

    infile.close()
    outfile.close()

def check_sum(isbn):
    acc = 0
    for i in range(len(isbn)):
        num = int(isbn[i]) * (10 - i)
        acc += num
    return acc % 11

def send_message(file, friend):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    for line in infile:
        outfile.write(line)

def send_safe_message(file, friend, key):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")

    for line in infile:
        new_line = encode(line, key)
        outfile.write(new_line)

def send_uncrackable_message(file, friend, pad):
    infile = open(file, "r")
    outfile = open(friend + ".txt", "w")
    padfile = open(pad, "r")
    key = padfile.read()

    for line in infile:
        new_line = encode_better(line, key)
        outfile.write(new_line)


def main():
    # add other function calls here
    number_words("monty.txt", "monty_outfile.txt")
    hourly_wages("wages.txt", "wages_outfile.txt")
    print(check_sum("0072946520"))
    send_message("monty.txt", "Arthur")
    send_safe_message("Arthur.txt", "Tim", 3)
    send_uncrackable_message("Arthur.txt","Lance","pad.txt")
    pass


main()
