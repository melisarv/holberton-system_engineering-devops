#!/usr/bin/python3
"""Python script to export data in the CSV format"""
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    users = get(url + "users/{}".format(user_id)).json()
    username = users.get("username")
    todos = get(url + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, e.get("completed"),
                          e.get("title")]) for e in todos]
