#!/usr/bin/python3
"""This module uses the JSONPlaceholder API to get information"""
import requests
import csv
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

        csv_filename = f"{id}.csv"
        with open(csv_filename, 'w') as csvfile:
            fieldnames = ["userId", "username", "completed", "title"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                    quoting=csv.QUOTE_ALL)
            for todo in todos:
                writer.writerow({"userId": id,
                                 "username": employee_name,
                                 "completed": todo["completed"],
                                 "title": todo["title"]})

        tasks = len(todos)
        done_tasks = 0
        for todo in todos:
            if todo["completed"]:
                done_tasks += 1

        print("Employee {} is done with tasks ({}/{}):"
              .format(employee_name, done_tasks, tasks))
        for todo in todos:
            if todo["completed"]:
                print("\t {}".format(todo["title"]))

    except requests.exceptions.RequestException as e:
        print(f"Oops error: {e}")


if __name__ == "__main__":
    user_id = int(sys.argv[1])
    get_employee_name_and_todo_progress(user_id)
