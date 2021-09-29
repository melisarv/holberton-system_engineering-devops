#!/usr/bin/python3
"""queries the Reddit API and return a list the titles of all hot articles"""
import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """return a list the titles"""
    url = 'https://www.reddit.com'
    query = '/r/' + subreddit + '/hot.json'
    res = requests.get(url+query,
                       params={"count": count, "after": after},
                       headers={"User-agent": "your bot 0.1"})
    if res.status_code != 200:
        return None

    result = res.json()
    h_list = hot_list + [i.get("data").get("title")
                         for i in result
                         .get("data")
                         .get("children")]

    if not result.get("data").get("after"):
        return h_list

    return recurse(subreddit, h_list, result.get("data").get("after"),
                   result.get("data").get("count"))
