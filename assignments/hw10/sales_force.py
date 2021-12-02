"""
Name: Benjamin Roth
sales_person.py

Problem: this program will store a sales person for a sales force and track their sales

Certification of Authenticity:
I verify that this assignment is entirely my own work.
"""
from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, file_name):
        infile = open(file_name, "r")
        for line in infile:
            sales_person = line.split(", ")
            s = SalesPerson(sales_person[0], sales_person[1])
            for sale in s.get_sales():
                s.enter_sale(sale)
            self.sales_people.append(s)

    def quota_report(self, quota):
        report = []
        for s in self.sales_people:
            employee_report = [s.get_id(), s.get_name(), s.total_sales(), s.met_quota(quota)]
            report.append(employee_report)
        return report

    def individual_sales(self, employee_id):
        id_list = []
        for s in self.sales_people:
            id_list.append(s.get_id())
        if employee_id in id_list:
            return SalesPerson
        return None
