#!/usr/bin/python3
"""Python script that returns information using REST API"""
import csv
import json
import requests
import sys


def fetch_user_todo_list(user_id):
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")

    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    json_data = {
        user_id: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            }
            for t in todos
        ]
    }

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)


if __name__ == "__main__":
    user_id = sys.argv[1]
    fetch_user_todo_list(user_id)
