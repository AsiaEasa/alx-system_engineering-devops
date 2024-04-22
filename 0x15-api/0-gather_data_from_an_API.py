#!/usr/bin/python3
"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv

def fetch_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    # Fetch user details
    user_response = requests.get(f"{base_url}users/{employee_id}")
    employee_name = user_response.json().get("name")

    if employee_name is not None:
        # Fetch todos
        todos_response = requests.get(f"{base_url}todos?userId={employee_id}").json()
        total_tasks = len(todos_response)
        completed_tasks = [task for task in todos_response if task.get("completed")]
        num_completed_tasks = len(completed_tasks)

        # Print progress
        print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task.get('title')}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script_name.py employee_id")
        exit(1)

    employee_id = argv[1]
    fetch_todo_progress(employee_id)
