"""
Name: Benjamin Roth
traffic.py

Problem: calculate and output the average number of vehicles traveled down each road per day
         as well as the total number of vehicles
         and the average number of vehicles for all of the roads

Certification of Authenticity:
I verify that this assignment is entirely my own work.
"""

# take inputs for number of roads
# take inputs for number of days surveyed
# write a for loop for the number of roads
#       write a for loop inside the roads loop
#       take inputs for number of cars travelled
# Print average number of cars travelled

def dot_traffic():
    road = int(input("How many roads are you surveying?"))
    tot_acc = 0
    for i in range(road):
        car_acc = 0
        day = int(input('How many days was road ' + str(i + 1) +" surveyed? "))
        for dayx in range(day):
            cars = int(input("How many cars travelled on day " + str(dayx + 1) + "? "))
            car_acc += cars
        print("Road " + str(i + 1) + " average vehicles per day: " + str(round(car_acc / day, 2)))
        tot_acc += car_acc
    print('Total number of vehicles traveled on all roads: ' + str(tot_acc))
    print('Average number of vehicles per road: ' + str(round(tot_acc / road, 2)))


def main():
    dot_traffic()

if __name__ == '__main__':
    main()
