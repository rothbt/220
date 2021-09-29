"""
Name: Benjamin Roth>
lab5.py
"""

from graphics import *
from math import *

def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()


    triangle = Polygon(p1, p2, p3)
    triangle.draw(win)

# find side lengths
    a = sqrt((p1.getX() - p2.getX()) ** 2 + (p1.getY() - p2.getY()) ** 2)
    b = sqrt((p1.getX() - p3.getY()) ** 2 + (p1.getX() - p3.getY()) ** 2)
    c = sqrt((p2.getX() - p3.getY()) ** 2 + (p2.getX() - p3.getY()) ** 2)

    s = a + b + c / 3
    area = sqrt(s * (s - a) * (s - b) * (s - c))


    area_pt = Point(win_width / 2, win_height - 20)
    perimeter_pt = Point(win_width / 2, win_height - 40)
    perimeter_txt = Text(perimeter_pt, "The perimeter of the triangle is: " + str(s))
    area_txt = Text(area_pt,"The area of the triangle is: " + str(area))
    area_txt.draw(win)
    perimeter_txt.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    red_box = Entry(Point(red_text_pt.getX() + 40, red_text_pt.getY()), 5)
    green_box = Entry(Point(green_text_pt.getX() + 40, green_text_pt.getY()), 5)
    blue_box = Entry(Point(blue_text_pt.getX() + 40, blue_text_pt.getY()), 5)

    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for i in range(5):
        win.getMouse()
        red = int(red_box.getText())
        green = int(green_box.getText())
        blue = int(blue_box.getText())
        color = color_rgb(red, green, blue)
        shape.setFill(color)


    # Wait for another click to exit
    win.getMouse()
    win.close()

def process_string():
    s = input("Enter a string: ")
    x = s[0]
    print(x)
    x = s[-1]
    print(x)
    x = s[2:6]
    print(x)
    x = s[0] + s[-1]
    print(x)
    x = s[:3] * 10
    print(x)
    for i in s:
        print(i)
    x = len(s)
    print(x)

def list_processing():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]

    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = str(values[1] * 5)
    print(x)
    values[4] = pt
    x = values[2:5]
    print(x)
    x = [values[2], values[3], values[0]]
    print(x)
    x = [values[2], values[0], float(values[-1])]
    print(x)
    sumx = sum(x)
    print(sumx)
    x = len(values)
    print(x)

def another_series():
    terms = int(input("Enter the number of terms: "))
    acc = 0
    for i in range(terms):
        y = 2 + 2 * (i % 3)
        print(y, end=" ")
        acc += y
    print()
    print(acc)



def main():
    # target()
    triangle()
    color_shape()
    process_string()
    list_processing()
    another_series()
    pass


main()
