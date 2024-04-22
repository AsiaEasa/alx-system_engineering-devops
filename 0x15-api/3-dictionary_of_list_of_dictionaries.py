#!/usr/bin/python3
"""Python script that returns information using REST API"""
import csv
import json
import requests
import sys


def fetch_all_todo_lists():
    URL = "https://jsonplaceholder.typicode.com/"

    ALL_USERS = requests.get(URL + "users").json()

    ALL_TASKS = {}

    for USER in ALL_USERS:
        USER_ID = USER["id"]
        USERNAME = USER["username"]
        TODOS = requests.get(URL + "todos", params={"userId": USER_ID}).json()
        USER_TASKS = [
            {
                "username": USERNAME,
                "task": t.get("title"),
                "completed": t.get("completed")
            }
            for t in TODOS
        ]
        ALL_TASKS[USER_ID] = USER_TASKS

    with open("todo_all_employees.json", "w") as JSONFILE:
        json.dump(ALL_TASKS, JSONFILE, indent=4)


if __name__ == "__main__":
    fetch_all_todo_lists()
