"""
Name: Benjamin Roth
lab7.py
"""
import math

def cash_conversion():
    int_input = int(input("What is the integer?: "))
    print("$" + '{:.2f}'.format(int_input))

def encode():
    message = input("What is the message?: ")
    key = int(input("What is the key?: "))
    acc = ''
    for c in message:
        x = ord(c)
        x += key
        new_c = chr(x)
        acc += new_c
    print(acc)

def sphere_area(radius):
    area = 4 * (math.pi) * radius ** 2
    return area

def sphere_volume(radius):
    volume = 4 / 3 * math.pi * radius ** 3
    return volume

def sum_n(n):
    acc = 0
    for i in range(n):
        acc += n

    return acc

def sum_n_cubes(n):
    acc = 0
    for i in range(n):
        acc = acc + i ** 3

    return acc

def encode_better():
    message = input("What is the message?: ")
    key = input("What is the key?: ")
    acc = ""
    for i in range(len(message)):
        c = ord(message[i])
        k = key[i % len(key)]
        k = ord(k) - 97
        c = c + k
        new_c = chr(c)
        acc += new_c
    print(acc)

def main():
    print(sphere_area(3))
    print(sphere_volume(3))
    print(sum_n(5))
    print(sum_n_cubes(5))

    encode_better()
    cash_conversion()
    encode()

    pass


main()
