#!/usr/bin/python3
"""Python script that returns information using REST API"""
import csv
import json
import requests
import sys


def fetch_user_todo_list(USER_ID):
    URL = "https://jsonplaceholder.typicode.com/"

    USER = requests.get(URL + "users/{}".format(USER_ID)).json()
    USERNAME = USER.get("username")

    TODOS = requests.get(URL + "todos", params={"userId": USER_ID}).json()

    JSON_DATA = {
        USER_ID: [
            {
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": USERNAME
            }
            for t in TODOS
        ]
    }

    with open("{}.json".format(USER_ID), "w") as JSONFILE:
        json.dump(JSON_DATA, JSONFILE, indent=4)


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    fetch_user_todo_list(USER_ID)
