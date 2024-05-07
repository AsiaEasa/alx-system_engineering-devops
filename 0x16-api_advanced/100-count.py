#!/usr/bin/python3
"""Module 100-count.py"""
import requests


def count_words(subreddit, word_list, titles=[], after=None):
    """queries the Reddit"""
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?after={after}"
    headers = {'User-Agent': 'Hi/0.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get('data')
        after = data.get("after")
        articles = data.get("children")
        for article in articles:
            titles.append(article.get("data").get("title"))
        count_words(subreddit, word_list, titles, after)
    else:
        count = {}
        word_list = [word.lower() for word in word_list]
        words = []
        for word in word_list:
            if word not in words:
                words.append(word)

        for title in titles:
            for word in words:
                words_in_title = [word.lower() for word in title.split(" ")]
                for word_in_title in words_in_title:
                    if word == word_in_title:
                        count[word] = count.get(word, 0) + 1
        count = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        if count is not {}:
            for item in count:
                print("{}: {}".format(item[0], item[1]))
