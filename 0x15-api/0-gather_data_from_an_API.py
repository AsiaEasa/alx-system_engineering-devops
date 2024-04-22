#!/usr/bin/python3
"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_tasks(employee_id):
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + "users/{}".format(employee_id)).json()

    PARM = {"userId": employee_id}
    todos = requests.get(URL + "todos", PARM).json()

    completed = [t.get("title") for t in todos if t.get("completed")]

    return user.get("name"), len(completed), len(todos), completed


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
    else:
        employee_id = input("Enter employee ID: ")
    name, completed_tasks, total_tasks, completed = \
        get_employee_tasks(employee_id)

    print("Employee {} is done with tasks({}/{}):".format(
        name, completed_tasks, total_tasks))

    [print("\t {}".format(task)) for task in completed]
