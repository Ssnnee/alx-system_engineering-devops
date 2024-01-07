#!/usr/bin/python3
"""This module uses the JSONPlaceholder API to get information"""
import requests
import sys


def get_employee_name_and_todo_progress(id):
    """This function gets information from JSONPlaceholder API"""
    url = "https://jsonplaceholder.typicode.com/users"
    todo_url = f"{url}/{id}/todos"

    try:
        user_res = requests.get(f"{url}/{id}")
        user_res.raise_for_status()
        uset_data = user_res.json()
        employee_name = uset_data["name"]

        todo_res = requests.get(todo_url)
        todo_res.raise_for_status()
        todos = todo_res.json()

        tasks = len(todos)
        done_tasks = 0
        for todo in todos:
            if todo["completed"]:
                done_tasks += 1

        print("Employee {} is done with tasks ({}/{}):"
              .format(employee_name, done_tasks, tasks))
        for todo in todos:
            if todo["completed"]:
                print(f"\t {todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Oops error: {e}")


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    get_employee_name_and_todo_progress(user_id)
