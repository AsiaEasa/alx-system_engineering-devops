#!/usr/bin/python3
"""handle requests"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    if not subreddit or type(subreddit) is not str:
        return 0
    url = f"http://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Hi/0.0'}
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        r = r.json()
    else:
        return 0
    return r['data']['subscribers']
