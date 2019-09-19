#!/usr/bin/python3
""" how many subscribers """
import requests


def recurse(subreddit, hot_list=[], after=''):
    """ returns the number of subscribers """
    url = 'https://www.reddit.com/r/{}/hot.json?after={}'.format(
          subreddit, after)
    agent007 = {'User-Agent': 'alexa_developer'}
    solicitud = requests.get(url, headers=agent007, allow_redirects=False)
    if solicitud.status_code == 200:
        soli = solicitud.json()
        datos = soli.get('data')
        hijos = datos.get('children')
        for x in hijos:
            post_datos = x.get('data')
            titulo = post_datos.get('title')
            hot_list.append(titulo)
        after = datos.get('after')
        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
