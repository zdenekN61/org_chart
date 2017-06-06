"""Main module"""

import argparse
import csv
import logging
import os
import re
import sys
from modules.departments import Department
from modules.employees import Employee
from modules.user_commands import UserCommands

__all__ = ["OrgChart"]

class OrgChart:
    # Init
    def __init__(self):
        self.readed_params = None
        self.arg_parser = None
        self.departments = None
        self.employees = None
        self.main()
    
    # Main call.
    def main(self):
        self._set_up_logging()
        self._read_and_check_params()
        self._process_params()
        self._read_user_commands()

    # Reads params.
    def _read_and_check_params(self):
        self.arg_parser = argparse.ArgumentParser(
                          description='Org chart + employees info.')
        self.arg_parser.add_argument('org_chart_file',
                                     type=argparse.FileType('r'),
                                     help='Path to org chart file(*.csv).')
        self.arg_parser.add_argument('employees_file',
                                     type=argparse.FileType('r'),
                                     help='Path to employees file(*.csv).')
        self.readed_params = self.arg_parser.parse_args()

    # Reads input data(use params).
    def _process_params(self):
        department_path = self.readed_params.org_chart_file.name
        department = Department()
        department.read_data(department_path)
        department.store_data()
        self.departments = department.department_data
        employees_path = self.readed_params.employees_file.name
        employee = Employee()
        employee.read_data(employees_path)
        employee.store_data()
        self.employees = employee.employees_data

    # User command.
    def _read_user_commands(self):
        user_input = UserCommands(self.departments, self.employees)
        user_input.start()

    # Sets up logging.
    def _set_up_logging(self):
        logging.basicConfig(filename='org_chart.log',
                            format='%(asctime)s-%(levelname)s-%(message)s',
                            datefmt='%m/%d/%Y %I:%M:%S',
                            filemode='a',
                            level=logging.DEBUG)

if __name__=='__main__':
    org_chart = OrgChart()
