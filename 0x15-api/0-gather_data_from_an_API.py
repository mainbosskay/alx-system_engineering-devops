#!/usr/bin/python3
"""Python script that uses REST API for a given employee ID"""
from re import fullmatch
from requests import get
from sys import argv


API_URL = "https://jsonplaceholder.typicode.com"
"""The RESTAPI's URL"""


if __name__ == "__main__":
    if len(argv) > 1:
        if fullmatch(r"\d+", argv[1]):
            empy_id = int(argv[1])
            empy_resp = get(f"{API_URL}/users/{empy_id}").json()
            tsk_rep = get(f"{API_URL}/todos").json()
            empy_name = empy_resp.get("name")
            tasks = list(filter(lambda k: k.get("userId") == empy_id, tsk_rep))
            comp_tasks = list(filter(lambda k: k.get("completed"), tasks))
            print(
                    f"Employee {empy_name} is done with "
                    f"tasks({len(comp_tasks)}/{len(tasks)}):"
            )
            for comp_task in comp_tasks:
                print(f"\t {comp_task.get('title')}")
