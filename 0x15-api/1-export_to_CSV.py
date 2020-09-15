#!/usr/bin/python3
""" REST Api"""
import requests
from sys import argv
import csv


if __name__ == '__main__':

    user_id = int(argv[1])
    URL = "https://jsonplaceholder.typicode.com"
    ep_user = "{}/users/{}".format(URL, user_id)
    ep_tasks = "{}/todos?userId={}".format(URL, user_id)
    EMPLOYEE = requests.get(ep_user).json()
    TASKS = requests.get(ep_tasks).json()
    USERNAME = EMPLOYEE.get("username")
    FILENAME = argv[1] + '.csv'

    with open(FILENAME, "w") as csv_f:
        wr = csv.writer(csv_f, quoting=csv.QUOTE_ALL)
        for task in TASKS:
            COMPLETED = task.get("completed")
            TITLE = task.get("title")
            wr.writerow([
                user_id,
                USERNAME,
                COMPLETED,
                TITLE
            ])
