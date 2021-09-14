# Project: 0x15-api

In this project you will find the files with solved cases to understand:

* What Bash scripting should not be used for
* What is an API
* What is a REST API
* What are microservices
* What is the CSV format
* What is the JSON format
* Pythonic Package and module name style
* Pythonic Class name style
* Pythonic Variable name style
* Pythonic Function name style
* Pythonic Constant name style
* Significance of CapWords or CamelCase in Python


## Contents
* 0-gather_data_from_an_API.py: Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.
* 1-export_to_CSV.py: Using what you did in the task #0, extend your Python script to export data in the CSV format:
** Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
** File name must be: USER_ID.csv
* 2-export_to_JSON.py: Using what you did in the task #0, extend your Python script to export data in the JSON format:
** Format must be: { "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
** File name must be: USER_ID.json
* 3-dictionary_of_list_of_dictionaries.py: Using what you did in the task #0, extend your Python script to export data in the JSON format:
** Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}
** File name must be: todo_all_employees.json

## Author
* Melisa Rojas
