#!/usr/bin/python3
"""Script that fetches info about a given employee's ID using an API"""
import json
import requests
import sys
from urllib.parse import urlencode

BASE_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <user_id>".format(sys.argv[0]))
        sys.exit(1)

    user_id = sys.argv[1]

    # Construct URL for fetching user info
    user_params = urlencode({'id': user_id})
    user_url = '{}/users?{}'.format(BASE_URL, user_params)

    # Fetch user info
    response = requests.get(user_url)
    if response.status_code != 200:
        print("Failed to fetch user info. Status code:", response.status_code)
        sys.exit(1)
    user_data = response.json()
    if not user_data:
        print("User not found.")
        sys.exit(1)
    user_info = user_data[0]
    user_name = user_info.get('name')

    # Construct URL for fetching user tasks
    tasks_params = urlencode({'userId': user_id})
    tasks_url = '{}/todos?{}'.format(BASE_URL, tasks_params)

    # Fetch user tasks
    response = requests.get(tasks_url)
    if response.status_code != 200:
        print("Failed to fetch user tasks. Status code:", response.status_code)
        sys.exit(1)
    tasks = response.json()

    # Process tasks
    completed_tasks = [task for task in tasks if task.get('completed')]
    completed_count = len(completed_tasks)
    total_tasks = len(tasks)

    # Print output
    print("Employee {} is done with tasks ({}/{}):".format(user_name, completed_count, total_tasks))
    for task in completed_tasks:
        print("\t{}".format(task.get('title')))
