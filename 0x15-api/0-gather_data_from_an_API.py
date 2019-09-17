#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv

if __name__ == '__main__':
    empleado = argv[1]
    informacion = 'https://jsonplaceholder.typicode.com/todos/'
    usuarios = 'https://jsonplaceholder.typicode.com/users/'
    info = requests.get(informacion, params={'userId': empleado})
    user = requests.get(usuarios, params={'id': empleado})
    todos = info.json()
    users = user.json()
    done = []
    total = len(todos)
    employee = users[0].get('name')

    for task in todos:
        if task.get('completed') is True:
            done.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(done), total))

    for task in done:
        print("\t {}".format(task.get('title')))
