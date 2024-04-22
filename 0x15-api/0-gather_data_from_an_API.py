#!/usr/bin/python3
"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

def get_employee_tasks(employee_id):
    # Base URL for the JSONPlaceholder API
    url = "https://jsonplaceholder.typicode.com/"

    # Get the employee information using the provided employee ID
    user = requests.get(url + "users/{}".format(employee_id)).json()

    # Get the to-do list for the employee using the provided employee ID
    params = {"userId": employee_id}
    todos = requests.get(url + "todos", params).json()

    # Filter completed tasks and count them
    completed = [t.get("title") for t in todos if t.get("completed") is True]

    # Return the employee's name and the number of completed tasks
    return user.get("name"), len(completed), len(todos), completed

if __name__ == "__main__":
    employee_id = sys.argv[1] if len(sys.argv) > 1 else input("Enter employee ID: ")
    name, completed_tasks, total_tasks, completed = get_employee_tasks(employee_id)

    # Print the employee's name and the number of completed tasks
    print("Employee {} is done with tasks({}/{}):".format(name, completed_tasks, total_tasks))

    # Print the completed tasks one by one with indentation
    [print("\t{}".format(task)) for task in completed]
