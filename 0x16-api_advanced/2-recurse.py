#!/usr/bin/python3
"""Module 2-recurse.py"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Queries the Reddit API"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    HEADERS = {'User-Agent': 'Hi/0.'}
    PARAMS = {'after': after} if after else {}

    R = requests.get(URL, headers=HEADERS, params=PARAMS)
    if R.status_code == 200:
        DATA = R.json()
        POSTS = DATA['data']['children']
        if POSTS:
            hot_list.extend([post['data']['title'] for post in POSTS])
            AFTER = DATA['data']['after']
            if AFTER:
                return recurse(subreddit, hot_list, AFTER)
            else:
                return hot_list
        else:
            return None
    else:
        return None
