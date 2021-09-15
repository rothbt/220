"""
Name: Benjamin Roth
lab3.py
"""

def average():
    grades = eval(input("How many grades are you entering?: "))
    acc = 0
    for i in range(grades):
       acc = acc + eval(input("what is the grade from homework" + str(i+1)))
    print(acc / grades)

#average()

def tip_jar():
    acc = 0
    for i in range(5):
        acc = acc + eval(input("How much did you give?"))
    print("the total in the jar is: $" + str(acc))

#tip_jar()


def newton():
    x = eval(input("what is the number x?"))
    refine = eval(input("how many times do you want to refine?"))
    approx = x/2

    for i in range(refine):
        approx = (approx + (x / approx))/2

    print(approx)

#newton()


def sequence():
    user = eval(input("How many terms do you want in the sequence?"))
    for i in range(1, user + 1):
        total = 1 + ((i//2) * 2)
        print(total)

#sequence()


def pi():
    #how many terms in seq; acc=1; for i in range(terms);inside: num = 2 + (x//2 * 2) denom = 1 + ((x + 1)//2 * 2))
    #print acc * 2
    terms = eval(input("what is 'n'?"))
    acc = 1
    for i in range(terms):
        num = 2 + ((i//2) * 2)
        den = 1 + (((i+1)//2) * 2)
        acc = acc * (num / den)

    print(acc * 2)

#pi()