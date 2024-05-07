#!/usr/bin/python3
"""Module 100-count.py"""

import requests


def count_words(subreddit, word_list, after=None, counts=None):
    if counts is None:
        counts = {}

    URL = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    HEADERS = {'User-Agent': 'Hi/0.0'}
    PARAMS = {'after': after} if after else {}

    RESPONSE = requests.get(URL, headers=HEADERS, params=PARAMS)
    if RESPONSE.status_code == 200:
        DATA = RESPONSE.json()
        POSTS = DATA['data']['children']
        for post in POSTS:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    X = word.lower()
                    Y = title.count(word.lower())
                    counts[X] = counts.get(X, 0) + Y

        after = DATA['data']['after']
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        return None
