#!/usr/bin/python3
""" how many subscribers """
import requests


def top_ten(subreddit):
    """ returns the number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent007 = {'User-Agent': 'alexa_developer'}
    solicitud = requests.get(url, headers=agent007, allow_redirects=False,
                             params={'limit': 10})
    if solicitud.status_code == 200:
        soli = solicitud.json()
        datos = soli.get('data')
        hijos = datos.get('children')
        if datos is not None and hijos is not None:
            for x in hijos:
                post_datos = x.get('data')
                titulo = post_datos.get('title')
                print(titulo)
    else:
        print('None')
