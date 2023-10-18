#!/usr/bin/env python3
"""
Defines a function `get_page`
"""
import redis
import requests
from datetime import timedelta


def get_page(url: str) -> str:
    """
    It uses the requests module to obtain
    the HTML content of a particular URL and returns it.
    Args:
        url (str): url whose content is to be fectched
    Returns:
        html (str): the HTML content of the url
    """
    r = redis.Redis()
    key = "count:{}{}{}".format('{', url, '}')
    r.incr(key)
    res = requests.get(url)
    r.setex(url, timedelta(seconds=10), res.text)
    return res.text
