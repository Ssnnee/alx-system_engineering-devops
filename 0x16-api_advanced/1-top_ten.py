#!/usr/bin/python3
"""This module contains a function that queries the Reddit API """
import requests


def top_ten(subreddit):
    """This function prints the titles of the first 10 hot
    posts listed for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        res = requests.get(url, headers=headers, allow_redirects=False)
        res.raise_for_status()

        for post in res.json().get("data").get("children"):
            print(post.get("data").get("title"))

    except requests.exceptions.RequestException:
        print(None)
