"""
Name: Benjamin Roth
bumper.py

Problem: this program draws two circles to a graphics window and randomizes their direction & rate
        the circles will change direction if they collide or hit the bounds of the window

Certification of Authenticity:
I verify that this assignment is entirely my own work.
"""

from random import randint
from graphics import Point, GraphWin, color_rgb, Circle


# int param. returns a random integer number in range [-move_amount,move_amount]
def get_random(move_amount):
    return randint(-move_amount, move_amount)


# returns a random color
def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color_choice = color_rgb(red, green, blue)
    return color_choice


def hit_vertical(ball, win):
    h_left = ball.getCenter().getX() - ball.getRadius() <= 0
    h_right = ball.getCenter().getX() + ball.getRadius() >= win.getWidth()
    return bool(h_right or h_left)


def hit_horizontal(ball, win):
    v_ceiling = ball.getCenter().getY() + ball.getRadius() >= win.getHeight()
    v_floor = ball.getCenter().getY() - ball.getRadius() <= 0
    return bool(v_ceiling or v_floor)


def did_collide(ball1, ball2):
    x_collide = abs(ball1.getCenter().getX() - ball2.getCenter().getX())
    y_collide = abs(ball1.getCenter().getY() - ball2.getCenter().getY())
    return bool(x_collide <= ball1.getRadius() and y_collide <= ball1.getRadius())


def bumper():
    win = GraphWin("Bumper", 600, 600)

    circle1 = Circle(Point(450, 300), 30)
    circle1.setFill(get_random_color())
    circle2 = Circle(Point(150, 300), 30)
    circle2.setFill(get_random_color())

    circle1.draw(win)
    circle2.draw(win)

    movement1 = [get_random(9), get_random(9)]
    movement2 = [get_random(9), get_random(9)]

    while True:
        if hit_horizontal(circle1, win):
            movement1[1] = - movement1[1]
        if hit_vertical(circle1, win):
            movement1[0] = - movement1[0]

        if hit_horizontal(circle2, win):
            movement2[1] = - movement2[1]
        if hit_vertical(circle2, win):
            movement2[0] = - movement2[0]

        if did_collide(circle1, circle2):
            movement1[0] = - movement1[0]
            movement1[1] = - movement1[1]
            movement2[0] = - movement2[0]
            movement2[1] = - movement2[1]

        circle1.move(movement1[0], movement1[1])
        circle2.move(movement2[0], movement2[1])


def main():
    bumper()


if __name__ == '__main__':
    main()
