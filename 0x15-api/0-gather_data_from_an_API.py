#!/usr/bin/python3
""" REST Api"""
import requests
from sys import argv


if __name__ == '__main__':

    user_id = int(argv[1])
    URL = "https://jsonplaceholder.typicode.com"
    ep_user = "{}/users/{}".format(URL, user_id)
    ep_tasks = "{}/todos?userId={}".format(URL, user_id)
    EMPLOYEE_NAME = requests.get(ep_user).json()
    TASKS = requests.get(ep_tasks).json()
    TOTAL_NUMBER_OF_TASKS = len(TASKS)
    DONE_TASKS = [task for task in TASKS if task.get('completed')]
    NUMBER_OF_DONE_TASKS = len(DONE_TASKS)
    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME.get('name'), NUMBER_OF_DONE_TASKS,
                  TOTAL_NUMBER_OF_TASKS))
    for task in DONE_TASKS:
        print('\t {}'.format(task.get('title')))
