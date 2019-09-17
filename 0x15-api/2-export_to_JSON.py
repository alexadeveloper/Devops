#!/usr/bin/python3
""" Gather data from an API """
import json
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
    taskxuser = {}
    employee = users[0].get('username')
    with open("{}.json".format(empleado), "w+") as jsonf:
        for task in todos:
            estado = task.get('completed')
            titulo = task.get('title')
            dic = {}
            dic['task'] = titulo
            dic['completed'] = estado
            dic['username'] = employee
            done.append(dic)
        taskxuser[empleado] = done
        datos = json.dumps(taskxuser)
        jsonf.write(datos)
