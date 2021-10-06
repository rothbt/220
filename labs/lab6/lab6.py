"""
Name: Benjamin Roth
lab6.py
"""


def name_reverse():
    x = input("What is your full name?")
    full = x.split(" ")
    print(full[1],", ", full[0])

def company_name():
    x = input("What is the url?: ")
    x = x.split(".")
    print(x[1])

def initials():
    n = int(input("How many students?: "))
    for i in range(1, n+1):
        first = input("What is the first name of student " + str(i))
        last = input("What is the last name of student " + str(i))
        initial = str(first[0]) + str(last[0])
        print(initial)

def names():
    x = input("What are the students names?: ")
    x = x.split(", ")
    for full in x:
        fulls = full.split(" ")
        first = fulls[0]
        last = fulls[1]
        initial = str(first[0]) + str(last[0])
        print(initial)

def thirds():
    n = int(input("How many sentences?: "))
    for _ in range(n):
        x = input("What is the sentence?: ")
        length = len(x)
        third = x[2: length:3]
        print(third)

def word_average():
    x = input("What is the sentence?")
    acc = 0
    words = x.split()

    for word in words:
        acc += len(word)
    acc = acc / len(words)
    print(acc)

def pig_latin():
    x = input("What sentence do you want to translate?: ")
    x.lower()
    words = x.split(" ")
    for word in words:
        pig = word[1:] + word[0] + "ay"
        print(pig)

def main():
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()

if __name__ == '__main__':
    main()
