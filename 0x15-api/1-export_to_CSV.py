#!/usr/bin/python3
""" Gather data from an API """
import requests
from sys import argv
import csv

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
    employee = users[0].get('username')
    with open("{}.csv".format(empleado), "a+") as csvf:
        csvfile = csv.writer(csvf, quoting=csv.QUOTE_ALL)
        for task in todos:
            estado = task['completed']
            titulo = task['title']
            csvfile.writerow(["{}".format(empleado),
                              "{}".format(employee),
                              "{}".format(estado),
                              "{}".format(titulo)])
