#!/usr/bin/python3
"""This module contains a function that queries the Reddit API """
import json
import requests


def number_of_subscribers(subreddit):
    """This function returns the number of subscribers of a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    res = requests.get(url, allow_redirects=False)

    if res.status_code != 200:
        return 0

    nbr_subs = json.loads(res.text).get("data").get("subscribers")
    return nbr_subs
