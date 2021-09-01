"""
Name: Benjamin Roth
lab1.py

Problem: This function calculates the area of a rectangle
"""

def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

#calc_rec_area()

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume =", volume)

#calc_volume()

def shooting_percentage():
    total_shots = eval(input("Enter the number of total shots: "))
    shots_made = eval(input("Enter the number of shots made: "))
    shot_percentage = shots_made / total_shots * 100
    print("Shooting Percentage =", shot_percentage)

#shooting_percentage()

def coffee():
    pounds = eval(input("Enter the number of pounds purchased: "))
    price_per_pound = 10.50
    shipping_cost_per_pound = .86
    total = pounds * price_per_pound + pounds * shipping_cost_per_pound + 1.5
    print("The total price is: ", total)

#coffee()

def kilometers_to_miles():
    user_input = eval(input("Enter the number of kilometers: "))
    miles = user_input / 1.61
    print("The number of miles is: ", miles)

kilometers_to_miles()



