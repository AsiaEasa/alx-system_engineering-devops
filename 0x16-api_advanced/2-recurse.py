#!/usr/bin/python3
"""Module 2-recurse.py"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """queries the Reddit API"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    headers = {'User-Agent': 'Hi/0.'}
    params = {'after': after} if after else {}

    r = requests.get(url, headers=headers, params=params)
    if r.status_code == 200:
        data = r.json()
        posts = data['data']['children']
        if posts:
            hot_list.extend([post['data']['title'] for post in posts])
            after = data['data']['after']
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
