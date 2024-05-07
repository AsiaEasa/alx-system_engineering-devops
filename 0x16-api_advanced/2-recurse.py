#!/usr/bin/python3
"""Module 2-recurse.py"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API"""
    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    HEAD = {'User-Agent': 'Hi/0.'}
    P = {'after': A} if A else {}

    R = requests.get(URL, headers=HEAD, params=P)
    if R.status_code == 200:
        D = R.json()
        PO = D['data']['children']
        if PO:
            hot_list.extend([post['data']['title'] for post in PO])
            A = D['data']['after']
            if A:
                return recurse(subreddit, hot_list, A)
            else:
                return hot_list
        else:
            return None
    else:
        return None
