#!/usr/bin/python3
"""script using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""
from requests import get
from sys import argv


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    users = get(url + 'users/{}'.format(argv[1])).json()
    todos = get(url + 'todos', params={'userId': argv[1]}).json()
    completed = [title.get("title") for title in todos if
                 title.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(users.get("name"),
                                                          len(completed),
                                                          len(todos)))
    [print("\t {}".format(title)) for title in completed]
