"""Processing employee file.
   - opens file
   - reads data
   - stores it into objects
"""

import csv
import logging
import os
import sys
from modules.employees_object import employee_object
from modules.read_csv import ReadCsv

__all__ = ["Employee"]

class Employee(ReadCsv):
    # Init.
    def __init__(self):
        self.raw_file_data = None
        self.employees_data = None

    # Reads data from the file.
    def read_data(self, employees_file):
        self.raw_file_data = self.read_file(employees_file)

    # Processes raw data from the file. 
    def store_data(self):
        self.employees_data = {}
        for row in self.raw_file_data:
            if row:
                # Checks data, eventually stores it.
                valided_data = self.check_data(row)
                if valided_data:
                    employee_data = employee_object()
                    dep_id = int(row[3])
                    employee_data['id'] = int(row[0])
                    employee_data['first_name'] = row[1].strip()
                    employee_data['last_name'] = row[2].strip()
                    employee_data['dep_id'] = dep_id
                    employee_data['birth_date'] = row[4].strip()
                    if dep_id in self.employees_data:
                        self.employees_data[dep_id].append(employee_data)
                    else:
                        self.employees_data[dep_id] = [employee_data]
                else:
                    message = """Employees - line: %s cannot be 
                                 processed.""" % row
                    logging.warning(message)

    # Checks if data has proper format(count, format, etc.).
    def check_data(self, item):
        valid_data = True
        # Length of data.
        if len(item) != 5:
            valid_data = False
            message = """Employees - line: %s wrong count of 
                         params.""" % item
            logging.error(message)
        # Proper type of data.
        if item[0] and not str(item[0]).isdigit():
            valid_data = False
            message = """Employees - line: %s , [0] param is
                         not valid.""" % item
            logging.error(message)
        # Checks dep-id.
        if item[3] and not item[3].isdigit():
            valid_data = False
            message = """Employees - line: %s , [3] param is
                         not valid.""" % item
            logging.error(message)
        return valid_data
