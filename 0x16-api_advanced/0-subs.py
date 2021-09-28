#!/usr/bin/python3
"""queries the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """return total subscribers"""
    url = 'https://www.reddit.com'
    query = '/r/' + subreddit + '/about.json'
    res = requests.get(url+query, headers={'User-agent': 'your bot 0.1'})
    if res.status_code != 200:
        return 0

    return res.json().get("data").get("subscribers")
