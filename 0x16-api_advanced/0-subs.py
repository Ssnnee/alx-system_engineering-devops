#!/usr/bin/python3
"""This module contains a function that queries the Reddit API """
import requests


def number_of_subscribers(subreddit):
    """This function returns the number of subscribers of a given subreddit """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        res.raise_for_status()

        nbr_subs = res.json().get("data").get("subscribers")
        return nbr_subs

    except requests.exceptions.RequestException:
        print("Oops error occured")
        return 0
