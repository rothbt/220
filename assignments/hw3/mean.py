"""
Name: Benjamin Roth
mean.py

Problem: This program will calculate the RMS Average, the Harmonic Mean and the Geometric Mean

Inputs: User specifies number of inputs & values within inputs

Outputs: RMS Average, Harmonic Mean, and Geometric Mean

Algorithm:
Program takes user input for "n" inputs
Algorithm will calculate means based on inputs
Algorithm will print out the solution for each of the means

Certification of Authenticity:
I verify that this assignment was mostly my own work. However, since I missed class this week,
I received some assistance from Tucker Kilcoyne
"""

import math

def main():
    inputs = []
    acc = 1
    arg = int(input("Enter the number of inputs: "))
    for i in range(1, arg + 1):
        values = int(input("value" + str(i) + " : "))
        inputs.append(values)

    sq_input = [x ** 2 for x in inputs]
    rms = math.sqrt(sum(sq_input) / arg)

    harmonic = [1 / x for x in inputs]
    harmonic_mean = arg / sum(harmonic)

    for item in inputs:
        acc *= item
    geometric_mean = acc ** (1 / arg)

    print(round(rms, 3))
    print(round(harmonic_mean, 3))
    print(round(geometric_mean, 3))

if __name__ == '__main__':
    main()
