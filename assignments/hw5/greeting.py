"""
Name: Benjamin Roth
greeting.py

Problem: write a program that creates a greeting card with moving graphics

Certification of Authenticity:
I verify that this assignment is entirely my own work.
"""
# create graphics window

# create "envelope" for "card"

# create "card"

# then

# create white rectangle for "card"
# move envelope outside of graphics window while displaying card

# display "happy valentines day!" and heart on card
# click to close

from time import sleep
from graphics import GraphWin, Polygon, Point, Text, Rectangle, Circle, Line

def main():
    win = GraphWin("Greeting Card", 600, 600, autoflush=False)
    win.setCoords(0.0, 0.0, 6.0, 6.0)

# draw the card
    card = Rectangle(Point(1, 3.75), Point(5, 1.5))
    card.setFill("pink")

    valentine = Text(Point(3, 2.75), "Happy Valentines Day!")
    valentine.setSize(36)

# draw closed envelope, rectangle with "closed" triangle
    env = Polygon(Point(.75, 4), Point(3, 2.75), Point(5.25, 4), Point(5.25, 1.5), Point(.75, 1.5))
    env.setFill("white")
    env.draw(win)

    closed = Polygon(Point(0.75, 4.0), Point(3.0, 2.5), Point(5.25, 4.0))
    closed.setFill("white")
    closed.draw(win)

# draw a heart
    circle_l = Circle(Point(2.75, 2.75), 0.25)
    circle_r = Circle(Point(3.25, 2.75), 0.25)
    circle_r.setOutline("red")
    circle_l.setOutline("red")
    circle_r.setFill("red")
    circle_l.setFill("red")

    triangle_heart = Polygon(Point(2.59, 2.55), Point(3, 2.75), Point(3.41, 2.55), Point(3.0, 2.15))
    triangle_heart.setFill("red")
    triangle_heart.setOutline("red")
    triangle_heart.draw(win)
    circle_r.draw(win)
    circle_l.draw(win)

# prompt user to click

    click_text = Text(Point(3.0, 5.0),"Click to open!")
    click_text.setSize(24)
    click_text.draw(win)
    win.update()

# open the envelope
    win.getMouse()
    sleep(.5)

# open envelope
    open_e = Polygon(Point(0.75, 4.0), Point(3.0, 5.5), Point(5.25, 4.0))
    open_e.setFill("white")

    # arrow carrying away heart
    fin = Polygon(Point(0, .25), Point(.25, .25), Point(.25, 0))
    fin.setWidth(4)
    fin.setFill("black")

    fin2 = fin.clone()
    arrowhead = fin.clone()
    fin3 = fin.clone()

    fin2.move(.25, .25)
    fin3.move(.5, .5)
    arrowhead.move(.75, .75)

    shaft = Line(Point(.25, .25), Point(1, 1),)
    shaft.setWidth(4)

    circle_l.undraw()
    circle_l.draw(win)
    triangle_heart.undraw()
    triangle_heart.draw(win)

    shaft.draw(win)
    arrowhead.draw(win)
    fin.draw(win)

    circle_r.undraw()
    circle_r.draw(win)

    for _ in range(8):
        shaft.move(.3, .25)
        arrowhead.move(.3, .25)
        fin.move(.3, .25)
        fin3.move(.3, .25)
        fin2.move(.3, .25)
        sleep(.1)
        win.update()

    for _ in range(12):
        shaft.move(.3, .25)
        arrowhead.move(.3, .25)
        fin.move(.3, .25)
        fin3.move(.3, .25)
        fin2.move(.3, .25)
        circle_l.move(.3, .25)
        circle_r.move(.3, .25)
        triangle_heart.move(.3, .25)
        sleep(.1)
        win.update()

    open_e.draw(win)
    card.draw(win)
    valentine.draw(win)
    env.undraw()
    env.draw(win)

    sleep(.5)
    win.update()

# move the envelope
    for _ in range(7):
        env.move(0, -1)
        open_e.move(0, -1)
        closed.move(0, -1)
        win.update()
        sleep(.2)

# click to close
    close_text = click_text
    close_text.setText("Click to close")
    win.update()

    win.getMouse()
    win.close()

if __name__ == '__main__':
    main()
