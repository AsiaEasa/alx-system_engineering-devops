#!/usr/bin/python3
"""
a python script that using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

def fetch_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    todo_url = f'{base_url}/{employee_id}/todos'

    try:
        response = requests.get(todo_url)
        response.raise_for_status()
        todos = response.json()
        
        completed_tasks = [todo['title'] for todo in todos if todo['completed']]
        total_tasks = len(todos)
        num_completed_tasks = len(completed_tasks)
        employee_name = todos[0]['name']  # Use 'name' field for employee name
        
        print(f"Employee {employee_name} is done with tasks({num_completed_tasks}/{total_tasks}):")
        for task in completed_tasks:
            print(f"\t{task}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_todo_progress(employee_id)
