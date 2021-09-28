#!/usr/bin/python3
"""queries the Reddit API and prints the titles of the first 10 posts"""
import requests


def top_ten(subreddit):
    """prints the top 10 hot posts"""
    url = 'https://www.reddit.com'
    query = '/r/' + subreddit + '/hot.json?limit=10'
    res = requests.get(url+query, headers={'User-agent': 'your bot 0.1'})
    if res.status_code != 200:
        print('None')
    else:
        for i in res.json().get("data").get("children"):
            print(i.get("data").get("title"))
