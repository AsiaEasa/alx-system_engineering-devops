#!/usr/bin/python3
"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


def fetch_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch data from the API.")
        return
    
    name = response.json().get("name")
    if name is not None:
        url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        todos_response = requests.get(url_todos)
        todos = todos_response.json()
        
        total_tasks = len(todos)
        completed_tasks = [todo for todo in todos if todo['completed']]
        num_completed_tasks = len(completed_tasks)
        
        print(f"Employee {name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python script_name.py employee_id")
        exit(1)
    
    employee_id = argv[1]
    fetch_todo_progress(employee_id)
