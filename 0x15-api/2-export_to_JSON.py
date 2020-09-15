#!/usr/bin/python3
""" REST Api"""
import json
import requests
from sys import argv


if __name__ == '__main__':

    user_id = int(argv[1])
    URL = "https://jsonplaceholder.typicode.com"
    ep_user = "{}/users/{}".format(URL, user_id)
    ep_tasks = "{}/todos?userId={}".format(URL, user_id)
    EMPLOYEE = requests.get(ep_user).json()
    TASKS = requests.get(ep_tasks).json()
    USERNAME = EMPLOYEE.get("username")
    FILENAME = argv[1] + '.json'

    list_tasks = []
    for task in TASKS:
        COMPLETED = task.get("completed")
        TITLE = task.get('title')
        dic = {'task': TITLE, 'completed': COMPLETED,
               'username': USERNAME}
        list_tasks.append(dic)
    d = {user_id: list_tasks}
    with open(FILENAME, 'w') as json_f:
        json.dump(d, json_f)
