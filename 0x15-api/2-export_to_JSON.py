#!/usr/bin/python3
"""extend task #0 Python script to export data in the JSON format"""
import json
from requests import get
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    users = get(url + 'users/{}'.format(user_id)).json()
    username = users.get("username")
    todos = get(url + 'todos', params={'user_id': user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{"task": e.get("title"),
                              "completed": e.get("completed"),
                              "username": username} for e in todos]},
                  jsonfile)
