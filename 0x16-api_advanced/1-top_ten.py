#!/usr/bin/python3
"""
Function that queries the Reddit API
"""
import requests


def top_ten(subreddit):
    """ returns the titles of the first 10 hotpost """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {
        "User-Agent": ("linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
                       "Mozilla / 5.0(Windows NT x.y; Win64; x64; rv:10.0)"
                       "Gecko / 20100101 Firefox / 10.0"
                       "Chrome/70.0.3538.77 Safari/537.36")
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        print('None')
        return 0
    else:
        for child in response.json().get('data').get('children'):
            print(child.get('data').get('title'))
