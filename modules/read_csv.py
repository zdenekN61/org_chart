"""Reads a csv file(Comma Separated Values)
   - reads file
   - returns data()

   Source: https://docs.python.org/3.5/library/csv.html
"""

import csv
import logging
import os

__all__ = ['ReadCsv']

class ReadCsv:
    # Reads data from the file.
    def read_file(self, file_path):
        data = []
        if os.path.exists(file_path):
            with open(file_path, newline='') as f:
                data = list(csv.reader(f, delimiter=';'))
            message = "File:%s readed successfully." % file_path
            logging.info(message)
        else:
            message = "File:%s doesnt exists." % file_path
            logging.error(message)
        return data
