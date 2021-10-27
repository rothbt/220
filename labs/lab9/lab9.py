"""
Name: Benjamin Roth
lab9.py
"""
from graphics import *
import math

def addTen(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def squareEach(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sumList(nums):
    acc = 0
    for i in range(len(nums)):
        acc += nums[i]
    return acc


def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def writeSumOfSquares():
    inf = input("What is the file name?")
    infile = open(inf, "r")
    outfile = open("outfile.txt", "w+")
    for line in infile:
        split_line = line.split()
        acc = 0
        for i in range(len(split_line)):
            split_line[i] = float(split_line[i]) ** 2
            acc += split_line[i]
        outfile.write("Sum = " + str(acc) + '\n')

def starter():
    weight = eval(input("What is the weight?"))
    numWins = eval(input("How many wins?"))

    if weight >= 155 and weight < 160 and numWins > 5:
        print("starter")
    elif weight > 199 or numWins > 20:
        print("starter")
    else:
        print("not a starter")

def leap_year(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        message = "it is a leap year"
        return message

    else:
        message = "it is not a leap year"
        return message

def circle_overlap():
    win = GraphWin("Cirle Shit", 400, 400)
    p1 = win.getMouse()
    p2 = win.getMouse()
    r = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    circle = Circle(p1, r)
    circle.draw(win)

    p3 = win.getMouse()
    p4 = win.getMouse()
    r2 = math.sqrt((p3.getX() - p4.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)
    circle2 = Circle(p3, r2)
    circle2.draw(win)

    overlap_message = Text(Point(200, 25), "The circles overlap")
    n_overlap = Text(Point(200, 25), "The circles do not overlap")

    distance = math.sqrt((p1.getX() - p2.getX()) ** 2 + (p3.getY() - p4.getY()) ** 2)

    if distance < (r + r2):
        overlap_message.draw(win)
    else:
        n_overlap.draw(win)

    win.getMouse()
    win.close()


def main():
    # add other function calls here
    x = [1, 2, 3]
    addTen(x)
    squareEach(x)
    print(sumList(x))
    toNumbers(x)
    writeSumOfSquares()
    starter()
    circle_overlap()
    pass


main()
