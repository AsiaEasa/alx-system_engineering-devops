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

    tasks = []
    for todo in todos:
        task_completed = "True" if todo["completed"] else "False"
        tasks.append([user["id"], user["name"], task_completed, todo["title"]])

    return tasks


if __name__ == "__main__":
    if len(sys.argv) > 1:
        employee_id = sys.argv[1]
    else:
        employee_id = input("Enter employee ID: ")

    tasks = get_employee_tasks(employee_id)

    filename = "{}.csv".format(employee_id)
    with open(filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(tasks)

    print("Data exported to", filename)
