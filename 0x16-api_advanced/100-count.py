#!/usr/bin/python3
"""parses the title of hot articles and prints a sorted count"""
import requests
import sys


def count_words(subreddit, word_list, after=None, count={}):
    """prints a sorted count of given keywords"""
    url = 'https://www.reddit.com'
    query = '/r/' + subreddit + '/hot.json'
    res = requests.get(url+query,
                       params={"after": after},
                       headers={"User-agent": "bot 0.1"})
    if res.status_code != 200:
        return None
    try:
        result = res.json().get("data").get("children")

        h_list = [i.get("data").get("title").lower().split()
                  for i in result]

        if not h_list:
            return None

        if count == {}:
            count = {w: 0 for w in word_list}

        for i in h_list:
            for w in word_list:
                if w.lower() == i[0]:
                    count[w] += 1

        after = res.json().get("data").get("after")

        if after is None:
            for x, y in sorted(count.items(),
                               key=lambda x: x[1],
                               reverse=False):
                if y != 0:
                    print("{}: {}".format(x, y))
        else:
            return count_words(subreddit, word_list, after, count)
    except:
        pass
