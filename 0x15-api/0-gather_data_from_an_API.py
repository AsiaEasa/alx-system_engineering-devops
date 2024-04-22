#!/usr/bin/python3
"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv

def get_user_completed_tasks(user_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    user_request = requests.get("{}users/{}".format(base_url, user_id))
    user_info = user_request.json()
    user_name = user_info.get("name")

    if user_name is not None:
        todos_request = requests.get("{}todos?userId={}".format(base_url, user_id))
        todos_info = todos_request.json()

        all_tasks = len(todos_info)
        completed_tasks = [task for task in todos_info if task.get("completed")]
        completed_count = len(completed_tasks)

        return user_name, completed_count, all_tasks, completed_tasks
    else:
        return None

if __name__ == "__main__":
    if len(argv) > 1:
        user_id = argv[1]
        user_info = get_user_completed_tasks(user_id)

        if user_info:
            user_name, completed_count, all_tasks, completed_tasks = user_info
            print("Employee {} is done with tasks({}/{}):".format(user_name, completed_count, all_tasks))

            for completed_task in completed_tasks:
                print("\t{}".format(completed_task.get("title")))
        else:
            print("User not found.")
