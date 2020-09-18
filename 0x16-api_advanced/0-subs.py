#!/usr/bin/python3
"""
Function that queries the Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """ returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": ("linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
                       "Mozilla / 5.0(Windows NT x.y; Win64; x64; rv:10.0)"
                       "Gecko / 20100101 Firefox / 10.0"
                       "Chrome/70.0.3538.77 Safari/537.36")
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
