#!/usr/bin/python3
""" how many subscribers """
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    agent007 = {'User-Agent': 'alexa_developer'}
    solicitud = requests.get(url, headers=agent007, allow_redirects=False)
    if solicitud.status_code == 200:
        soli = solicitud.json()
        datos = soli.get('data')
        subscribers = datos.get('subscribers')
        if datos is not None and subscribers is not None:
            return subscribers
    return 0
