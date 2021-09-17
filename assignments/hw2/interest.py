"""
Name: Benjamin Roth
interest.py

Problem: calculate and output the monthly interest charge for a credit card

Certification of Authenticity:
I verify that this assignment is entirely my own work.
"""

def main():
    month_int = eval(input("Enter the annual interest rate: "))/12
    bill_cyc = eval(input("Enter the # of days in billing cycle: "))
    net_bal = eval(input("Enter the previous balance: "))
    pay = eval(input("Enter the payment amount: "))
    day_of = eval(input("Enter the day of the billing cycle that the payment was made: "))
    month_charge = month_int / 100 * (((net_bal * bill_cyc) - (pay * (bill_cyc - day_of)))/bill_cyc)
    print(round(month_charge, 2))
if __name__ == '__main__':
    main()
