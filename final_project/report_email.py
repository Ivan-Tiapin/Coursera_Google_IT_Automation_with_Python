#!/usr/bin/env python3
"""Generates report and sends it to customer"""
import reports
import datetime
import os
import emails

def main():
    date_of_report= datetime.datetime.today().strftime("%B %d, %Y")
    print(date_of_report)
    home_dir = os.path.expanduser("~")
    texts_dir = os.path.join(home_dir, "supplier-data/descriptions", "")
    descritpions = []
    for file in os.listdir(texts_dir):
        with open(texts_dir + file) as text_file:
            text = text_file.readlines()
            name = text[0].strip()
            weight= text[1].strip()
            text_for_pdf = "name: {}<br/>weight: {}".format(name,weight)
            print(text_for_pdf)
            descritpions.append(text_for_pdf)
    reports.generate_report("/tmp/processed.pdf","Processed Update on {}<br/><br/>".format(date_of_report),
                            "<br/><br/>".join(descritpions))
    message = emails.generate_email("automation@example.com", "student-00-77d3d782c077@example.com",
                              "Upload Completed - Online Fruit Store",
                              "All fruits are uploaded tou our website successfully.A detailed list is attached to this email.",
                              "/tmp/processed.pdf")
    emails.send_email(message)

if __name__ == "__main__":
  main()

