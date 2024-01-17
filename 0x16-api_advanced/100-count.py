#!/usr/bin/python3
"""This module contains a function that queries the Reddit API """
import requests
import json
from collections import Counter


def count_words(subreddit, word_list, after=None):
    """This function  parses the title of all hot articles, and prints a
    sorted count of given keywords"""

    def count_helper(subreddit, word_list, after=None, counter=None):
        """This helper function parses the title of all hot articles, and"""
        url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

        if counter is None:
            counter = Counter()
        params = {'limit': 100}
        if after:
            params['after'] = after
        res = requests.get(url, params=params, allow_redirects=False)

        if res.status_code != 200:
            return counter

        data = json.loads(res.text)

        for i in range(len(data['data']['children'])):
            ttle = data['data']['children'][i]['data']['title'].lower().split()
            for w in word_list:
                if w in ttle and w not in ["java.", "java!", "java_"]:
                    counter[w] += 1

        if 'after' in data['data']:
            return count_helper(subreddit, word_list, data['data']['after'],
                                counter)
        else:
            return counter

    counter = count_helper(subreddit, word_list, after)
    for k, v in sorted(counter.items(), key=lambda x: (-x[1], x[0])):
        print("{}: {}".format(k, v))
