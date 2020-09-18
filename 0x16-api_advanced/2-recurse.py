#!/usr/bin/python3
"""
Function that queries the Reddit API
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ returns the titles of the first 10 hotpost """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=500'.format(subreddit)
    headers = {
        "User-Agent": ("linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
                       "Mozilla / 5.0(Windows NT x.y; Win64; x64; rv:10.0)"
                       "Gecko / 20100101 Firefox / 10.0"
                       "Chrome/70.0.3538.77 Safari/537.36")
    }
    param = {
        "after": after,
    }
    response = requests.get(url, headers=headers, params=param,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    if len(response.json().get('data').get('children')) < 1:
        return hot_list
    else:
        posts = response.json().get("data").get("children")
        hot_list += [post.get("data").get("title") for post in posts]
        after = response.json().get("data").get("after")
        if after is not None:
            recurse(subreddit, hot_list, after)
        return hot_list
