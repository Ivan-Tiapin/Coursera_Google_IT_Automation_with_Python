#!/usr/bin/env python3
""" Checks amount of specified errors in syslog.log by type and by user"""
import re
import operator
import csv

error={}
per_user={}

with open("syslog.log") as log:
  log_content=log.readlines()
  for line in log_content:
    line=line.strip()
    if "ERROR" in line:
      username=re.search("\((.+)\)",line).group(1)
      error_text=re.search("ERROR ([\w ]+)",line).group(1).strip()
      error[error_text]=error.get(error_text,0)+1
      current_count=per_user.get(username,[0,0])
      per_user[username]=[current_count[0],current_count[1]+1]
    elif "INFO" in line:
      username=re.search("\((.+)\)",line).group(1)
      current_count=per_user.get(username,[0,0])
      per_user[username]=[current_count[0]+1,current_count[1]]

per_user=[("Username",["INFO","ERROR"])]+sorted(per_user.items())
error=[("Error","Count")]+sorted(error.items(), key = operator.itemgetter(1), reverse=True)

with open("error_message.csv","w") as csv_file:
  writer = csv.writer(csv_file)
  for element in error:
    writer.writerow([element[0],element[1]])

with open("user_statistics.csv","w") as csv_file:
  writer = csv.writer(csv_file)
  for element in per_user:
    user,info,error = element[0],element[1][0],element[1][1]
    writer.writerow([user,info,error])