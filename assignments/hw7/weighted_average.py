"""
Name: Benjamin Roth
weighted_average.py

Problem: this program read a text file with students grades, and return an average for each student
    as well as collect errors for incorrect entry

Certification of Authenticity:
I verify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):

    in_file = open(in_file_name, 'r')
    out_file = open(out_file_name, 'w')

    # split line of file into student name , grades/weights
    for line in in_file:
        split_line = line.split(":")
        full_name = split_line[0]
        grades = split_line[1]
        grades_i = grades.split()

        # collect accumulator of weights for later exceptions
        weight_sum = 0
        for s in range(0, len(grades_i), 2):
            weight = int(grades_i[s])
            weight_sum += weight

        # in each student's grades/weights, calculate each test's weighted score
        student_weighted = 0
        for w in range(0, len(grades_i) - 1, 2):
            g = w + 1
            weighted_grade = int(grades_i[g]) * int(grades_i[w]) / 100
            student_weighted += weighted_grade

        # throw exception to user for incorrect entry
        if weight_sum == 100:
            out_file.write(full_name + "'s average: " + str(round(student_weighted, 1)) + '\n')

        elif weight_sum > 100:
            out_file.write(full_name + "'s average: " + "Error: The weights are more than 100." + '\n')

        else:
            out_file.write(full_name + "'s average: " + "Error: The weights are less than 100." + '\n')

    in_file.close()
    out_file.close()


def main():
    weighted_average('grades.txt', 'avg.txt')


if __name__ == '__main__':
    main()
