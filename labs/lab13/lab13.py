"""
Name: Benjamin Roth
lab13.py
"""


def is_in_binary(value, values):
    mid_value = values[len(values) // 2]
    while mid_value != value and len(values) > 1:
        if mid_value > value:
            values = values[:len(values) // 2]
        elif mid_value < value:
            values = values[len(values) // 2 + 1:]
        mid_value = values[len(values) // 2]
    if mid_value == value:
        return True
    else:
        return False


def selection_search(values):
    for i in range(len(values)):
        lowest_value = values[i]
        position = i
        for j in range(i, len(values)):
            if values[j] < lowest_value:
                lowest_value = values[j]
                position = values.index(j)
        values[i], values[position] = values[position], values[i]


def rect_sort(rectangles):
    d = {}
    areas = []
    for rect in rectangles:
        d[rect.get_area(rect)] = rect
        areas.append(get_area(rect))
    selection_search(areas)
    for i in range(len(areas)):
        rectangles[i] = d[areas[i]]
    print(areas)


def get_area(rectangle):
    p1 = rectangle.getP1()
    p2 = rectangle.getP2()
    w = abs(p1.getX() - p2.getX())
    h = abs(p1.getY() - p2.getY())
    return w + h


def trade_alert(file_name):
    infile = open(file_name, "r")
    data = infile.read().split()
    second = 0
    for num in data:
        number = int(num)
        second += number + 1
        if number > 830:
            print("Alert!")
            print(f"current second is {second + 1}")
        elif number > 500:
            print('warning!')


def main():
    # is_in_binary()
    iib_values = [1, 2, 3, 4, 5]
    value = 1
    print(is_in_binary(value, iib_values))
    pass


if __name__ == '__main__':
    main()
