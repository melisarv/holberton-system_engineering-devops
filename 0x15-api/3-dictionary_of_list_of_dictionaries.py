#!/usr/bin/python3
"""extend task #0 Python script to export data in the JSON format"""
import json
from requests import get
from sys import argv


if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({u.get("id"): [{
            "username": u.get("username"),
            "task": e.get("title"),
            "completed": e.get("completed")
        } for e in get(url + "todos",
                       params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
