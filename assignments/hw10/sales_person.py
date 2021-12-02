"""
Name: Benjamin Roth
sales_person.py

Problem: this program will store a class for a sales_person

Certification of Authenticity:
I verify that this assignment is entirely my own work.
"""

# create a class


class SalesPerson:
    # emp_id -> int
    # name (full) -> string
    # sales -> list of floats

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return int(self.employee_id)

    def get_name(self):
        return str(self.name)

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        flt_sale = float(sale)
        self.sales.append(flt_sale)

    def total_sales(self):
        sales_total = 0
        for sale in range(len(self.sales)):
            sales_total += sale
        return sales_total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() >= float(quota):
            return True
        return False

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() < other.total_sales():
            return -1
        return 0

    def __str__(self):
        return "{0} - {1}: {2}".format(self.employee_id, self.name, self.total_sales())