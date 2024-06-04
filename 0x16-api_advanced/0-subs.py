#!/usr/bin/python
"""Module for interacting with the Reddit API to fetch data"""
from requests import get


URL_REDDIT = "https://www.reddit.com"
"""The API URL for Reddit"""


def number_of_subscribers(subreddit):
    """Retrieves and returns subscribers count for specified subreddit"""
    head_reddit = {
        "Accept": "applcation/json",
        "User_Agent": " ".join([
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.7.4)",
            "Firefox/124.0.2",
            "safari/17.4.1"
            ])
    }
    resquest_data = get(
            f"{URL_REDDIT}/r/{subreddit}/about.json",
            headers=head_reddit,
            allow_redirects=False
    )
    if resquest_data.status_code == 200:
        return resquest_data.json()["data"]["subscribers"]
    return 0
