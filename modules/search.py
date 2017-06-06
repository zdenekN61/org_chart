"""Search for requested informations"""

from datetime import datetime
import logging
import os
import re

__all__ = ["SearchData"]

class SearchData:
    # Init.
    def __init__(self, departments, employees):
        self.employees = employees
        self.departments = departments

    # Searches 'Department'.
    def _search_department(self, dep_id):
        dep_id = int(dep_id)
        if dep_id in self.departments:
            name = self.departments[dep_id]["dep_name"]
            city = self.departments[dep_id]["dep_city"]
            result = "%s, %s" % (name, city)
            return result
        else:
            message = "Unknow department's id: %s." % dep_id
            logging.warning(message)

    # Searches 'Avgage'.
    def _search_avgage(self, dep_id):
        all_employees = self._all_employees(dep_id)
        years_all = 0.0
        year_long = 365.25*24*60*60
        employees_count = 0
        result = None
        today_date = datetime.today()
        for employee in all_employees:
            try:
                s_date = datetime.strptime(employee['birth_date'], '%d.%m.%Y')
                diff_time = (today_date-s_date).total_seconds()
                years_all += diff_time
                employees_count += 1
            except:
                message = """Invalid date: %s""" % employee['birth_date']
                logging.warning(message)
        if all_employees and (employees_count > 0) and years_all > 0:
            avgage = (years_all/(year_long))/employees_count
            result = "%.2f years" % (avgage)
        else:
            message = """Avg age is negative/invalid, its wrong."""
            logging.error(message)
        return result

    # Searches 'Count'.
    def _search_count(self, dep_id):
        all_employees = self._all_employees(dep_id)
        employees_count = len(all_employees)
        result = "%s" % employees_count
        return result

    # Searches 'People'.
    def _search_people(self, dep_id):
        all_employees = self._all_employees(dep_id)
        employees_names = ""
        for names in all_employees:
            employees_names += "%s %s, " % (names['first_name'],
                                            names['last_name'])
        result = "%s" % employees_names
        return result

    # Finds all employees for given id(loop).
    def _all_employees(self, dep_id):
        employees_list = []
        dep_id = int(dep_id)
        if dep_id in self.departments:
            dep_ids = self.departments[dep_id]["sub_dep_id"]
            dep_ids.append(dep_id)# ids
            for id_item in dep_ids:
                if id_item in self.employees:
                    employees_list += self.employees[id_item]
        else:
            message = "Unknow department id: %s." % dep_id
            logging.warning(message)
        return employees_list

