#!/usr/bin/python3
"""This module contains a recursive function that queries the Reddit API """
import json
import requests


def recurse(subreddit, hot_list=[], after=""):
    """This function returns a list containing the titles of all hot articles
    for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 100}

    if after:
        params['after'] = after

    res = requests.get(url, params=params, allow_redirects=False,)

    if res.status_code != 200:
        return None

    data = json.loads(res.text)

    for i in range(len(data['data']['children'])):
        hot_list.append(data['data']['children'][i]['data']['title'])
    if 'after' in data['data']:
        recurse(subreddit, hot_list, data['data']['after'])
    return hot_list
