"""
Name: Benjamin Roth
lab2.py
"""

def sum_of_threes():
    bound = int(input("bound?: "))
    accum = 0
    for i in range(0, bound + 1, 3):
        accum += i
    print(accum)

#sum_of_threes()

def multiplication_table():
    for h in range(1, 11):
        for l in range(1, 11):
            print(h * l, end=" ")
        print()

#multiplication_table()


def triangle_area():
    import math
    a = int(input("side a?"))
    b = int(input("side b?"))
    c = int(input("side c?"))

    s = (a + b + c)/2
    A = math.sqrt(s * (s - a) * (s - b) * (s - c))

    print("The area equals: ", A)

#triangle_area()

def sumSquares():
    import math
    lower_bound = int(input("lower bound?"))
    upper_bound = int(input("upper bound?"))
    acc = 0
    for i in range(lower_bound, upper_bound + 1):
        acc = acc + i ** 2
    print(acc)

#sumSquares()

def power():
    base = int(input("base?"))
    power = int(input("power?"))
    acc = 1
    for i in range(power):
        acc *= base
    print(acc)

#power()









