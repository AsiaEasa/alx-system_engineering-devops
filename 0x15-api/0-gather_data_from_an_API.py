#!/usr/bin/python3
"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def fetch_todo_progress(employee_id):
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Failed to fetch data from the API.")
        return
    
    todos = response.json()
    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    employee_name = todos[0]['name']
    
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py employee_id")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    fetch_todo_progress(employee_id)
