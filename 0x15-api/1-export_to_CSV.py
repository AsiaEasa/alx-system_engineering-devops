#!/usr/bin/python3
"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def get_employee_tasks(employee_id):
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + "users/{}".format(employee_id)).json()
    PARAMS = {"userId": employee_id}
    todos = requests.get(URL + "todos", PARAMS).json()
    tasks = [[employee_id, user["username"], "True" if todo["completed"] else "False", todo["title"]] for todo in todos]
    return tasks

if __name__ == "__main__":
    employee_id = sys.argv[1] if len(sys.argv) > 1 else input("Enter employee ID: ")
    tasks = get_employee_tasks(employee_id)
    with open("{}.csv".format(employee_id), "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(tasks)
