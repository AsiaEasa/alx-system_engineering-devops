#!/usr/bin/python3
"""handle requests"""
import requests


def number_of_subscribers(subreddit):
    """queries the Reddit API"""
    if not subreddit or type(subreddit) is not str:
        return 0
    URL = f"http://www.reddit.com/r/{subreddit}/about.json"
    HEAD = {'User-Agent': 'Hi/0.0'}
    R = requests.get(URL, headers=HEAD)
    if R.status_code == 200:
        R = R.json()
    else:
        return 0
    return R['data']['subscribers']
