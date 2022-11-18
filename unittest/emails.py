#!/usr/bin/env python3
"""Checks user_emails.csv for presence of email inputted as command line argument"""
import csv
import sys

# Creates dictionary that contains data from .csv file
def populate_dictionary(filename):
    email_dict = {}
    with open(filename) as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            name = str(row[0].lower())
            email_dict[name] = row[1]
    return email_dict

# Checks for present of specified email in chosen .csv file
def find_email(argv):
    try:
        fullname = str(argv[1] + " " + argv[2])
        # Preprocess the data
        email_dict = populate_dictionary('user_emails.csv')
        # If email exists, print it
        if email_dict.get(fullname.lower()):
            return email_dict.get(fullname.lower())
        else:
            return "No email address found"
    except IndexError:
        return "Missing parameters"

def main():
    # If data was inputted as command line argument - uses it, if not - uses default fullname.
    if len(sys.argv) == 1:
        data = ["", "Madison", "Mcintosh"]
    else:
        data = sys.argv
    print(find_email(data))

if __name__ == "__main__":
    main()
