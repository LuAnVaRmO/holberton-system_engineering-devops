#!/usr/bin/python3
""" REST Api"""
import json
import requests


if __name__ == '__main__':
    """ Requesting all data of all employee"""
    URL = "https://jsonplaceholder.typicode.com"
    ep_user = "{}/users/".format(URL)
    ep_tasks = "{}/todos".format(URL)
    EMPLOYEE = requests.get(ep_user).json()
    TASKS = requests.get(ep_tasks).json()
    FILENAME = 'todo_all_employees.json'

    user_dic = {}
    for user in EMPLOYEE:
        user_id = user.get('id')
        list_tasks = []
        for task in TASKS:
            if user_id == task.get('userId'):
                COMPLETED = task.get("completed")
                TITLE = task.get('title')
                USERNAME = user.get('username')
                dic = {'task': TITLE, 'completed': COMPLETED,
                       'username': USERNAME}
                list_tasks.append(dic)
        user_dic[user_id] = list_tasks

    with open(FILENAME, 'w') as json_f:
        json.dump(user_dic, json_f)
