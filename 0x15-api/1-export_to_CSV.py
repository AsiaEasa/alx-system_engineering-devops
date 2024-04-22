#!/usr/bin/python3
"""
A Python script that uses this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import csv
import requests
import sys


def fetch_user_todo_list(USER_ID):
    URL = "https://jsonplaceholder.typicode.com/"

    USER = requests.get(URL + "users/{}".format(USER_ID)).json()

    USERNAME = USER.get("username")

    TODOS = requests.get(URL + "todos", params={"userId": USER_ID}).json()

    with open("{}.csv".format(USER_ID), "w", newline="") as CSVFILE:
        WRITER = csv.writer(CSVFILE, quoting=csv.QUOTE_ALL)
        [WRITER.writerow(
            [USER_ID, USERNAME, t.get("completed"), t.get("title")]
        ) for t in TODOS]


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    fetch_user_todo_list(USER_ID)
