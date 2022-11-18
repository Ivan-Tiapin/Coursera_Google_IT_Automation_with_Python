#!/usr/bin/env python3
"""Searches for specified error in log file, inputted as command line argument"""
import sys
import os
import re

# Request error name(s) and searches for lines containing it/them
def error_search(log_file):
    error = input("What is the error? Input all error names using whitespaces")
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors

# Writes new log file, that contains only lines with specified name(s) of error
def file_output(returned_errors):
    with open(os.getcwd()+"/errors_found.log", 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


if __name__ == "__main__":
    log_file = ""
    # If log file was inputted as command line argument - uses it, if not - uses specified log file.
    if len(sys.argv) == 1:
        log_file = os.getcwd()+"/fishy.log"
    else:
        log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
