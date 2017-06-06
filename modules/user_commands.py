"""Processing user commands
   - command exists
   - searches for data
"""

import os
import logging
import re
import sys
from modules.show_help import show_help
from modules.search import SearchData

__all__ = ["UserCommands"]

SUPPORTED_COMMANDS = ['department', 'count', 'people', 'avgage', 'exit', 'help']

class UserCommands:
    # Init.
    def __init__(self, departments, employees):
        self.departments = departments
        self.employees = employees
        self.search = SearchData(self.departments, self.employees)

    # Start waiting for user commands.
    def start(self):
        show_help()
        while(True):
            print ('User Command:')
            command = input()
            command = command.lower()
            list_of_comm = self._read_command(command)
            comm_checked = self._check_command(list_of_comm)
            if comm_checked:
                if list_of_comm[0] == 'department':
                    self._command_department(list_of_comm[1])
                elif list_of_comm[0] == 'count':
                    self._command_count(list_of_comm[1])
                elif list_of_comm[0] == 'people':
                    self._command_people(list_of_comm[1])
                elif list_of_comm[0] == 'avgage':
                    self._command_avgage(list_of_comm[1])
                elif list_of_comm[0] == 'help':
                    self._command_help()
                elif list_of_comm[0] == 'exit':
                    self._command_exit()
            else:
                message = "Unknown user's command: %s" % command
                logging.warning(message)
                self._command_help()

    # Command 'Department'.
    def _command_department(self, dep_id):
        result = self.search._search_department(dep_id)
        print (result)

    # Command 'Count'.
    def _command_count(self, dep_id):
        result = self.search._search_count(dep_id)
        print (result)

    # Command 'People'.
    def _command_people(self, dep_id):
        result = self.search._search_people(dep_id)
        print (result)

    # Command 'Avgage'.
    def _command_avgage(self, dep_id):
        result = self.search._search_avgage(dep_id)
        print (result)

    # Command 'Help'.
    def _command_help(self):
        help_m = show_help()
        print (help_m)

    # Command 'Exit'.
    def _command_exit(self):
        message = "Used user command: exit"
        logging.info(message)
        sys.exit()
        
    # Reads command, preparing for check.
    def _read_command(self, command):
        comm = re.split(' ', command)
        return comm

    # Checks command(count, type, supported).
    def _check_command(self, command):
        valid = True
        if len(command) == 2:
            if command[0] not in SUPPORTED_COMMANDS:
                valid = False
            # Just check if is digit.
            if not str(command[1]).isdigit():
                valid = False
            else:
                if isinstance(command[1], float):
                    valid = False
        elif len(command) is 1:
            if command[0] not in SUPPORTED_COMMANDS:
                valid = False
        else:
            valid = False
        return valid
