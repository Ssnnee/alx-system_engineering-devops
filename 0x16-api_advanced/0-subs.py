#!/usr/bin/python3
"""This module contains a function that queries the Reddit API """
import json
import requests


def number_of_subscribers(subreddit):
    """This function returns the number of subscribers of a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    if res.status_code != 200:
        return 0

    if res.status_code == 302:
        return 0

    data = json.loads(res.text)

    if data is None:
        return 0

    if "data" not in data:
        return 0

    if "subscribers" not in data.get("data"):
        return 0

    return data.get("data").get("subscribers")
