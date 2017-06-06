"""Processing department file.
   - opens file
   - reads data
   - stores it into objects
"""

import logging
import os
import re
import sys
from modules.departments_object import department_object
from modules.read_csv import ReadCsv

__all__ = ["Department"]

class Department(ReadCsv):
    # Init.
    def __init__(self):
        self.raw_file_data = None
        self.department_data = None

    # Reads data from file.
    def read_data(self, department_file):
        self.raw_file_data = self.read_file(department_file)

    # Processes raw data from file. 
    def store_data(self):
        self.department_data = {}
        for row in self.raw_file_data:
            if row:
                # Checks data, eventually stores it.
                valided_data = self.check_data(row)
                if valided_data:
                    department_data = department_object()
                    dep_id = int(row[0])
                    department_data['id'] = dep_id
                    department_data['dep_name'] = row[2].strip()
                    department_data['dep_city'] = row[3].strip()
                    # Flag if department is sub-department as well.
                    # Checks if parend-id exists(its sub-department).
                    if row[1]:
                        department_data['parent_id'] = int(row[1])
                        # If is sub-dep, add link to its parent.
                        parent_id = department_data['parent_id']
                        while (parent_id):
                            if parent_id in self.department_data:
                                (self.department_data[parent_id]
                                                     ["sub_dep_id"].append(
                                                                    dep_id))
                                parent_id =(self.department_data[parent_id]
                                                                ['parent_id'])
                    self.department_data[dep_id] = department_data
                else:
                    message = """Departments - line: %s cannot be 
                                 processed.""" % row
                    logging.warning(message)

    # Checks if data has proper format(count, format, etc.).
    def check_data(self, item):
        valid_data = True
        # Length of data.
        if len(item) != 4:
            valid_data = False
            message = """Departments - line: %s wrong count of 
                         params.""" % item
            logging.error(message)
        # Proper type of data.
        if item[0] and not str(item[0]).isdigit():
            valid_data = False
            message = """Departments - line: %s , [0] param is
                         not valid.""" % item
            logging.error(message)
        # Checks dep-id.
        if item[1] and not item[1].isdigit():
            valid_data = False
            message = """Departments - line: %s , [3] param is
                         not valid.""" % item
            logging.error(message)
        return valid_data
