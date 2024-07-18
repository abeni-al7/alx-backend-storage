#!/usr/bin/env python3
'''Scrape the web and store the count of function calls'''
import requests
import redis
from functools import wraps
from typing import Callable

r = redis.Redis()
def count_calls(fn: Callable) -> Callable:
    '''Decorator for counting the number of calls to fn'''
    @wraps(fn)
    def wrapper(url):
        '''Increments count of calls in redis'''
        key = 'count:' + url
        r.incr(key)
        r.expire(key, 10)
        return fn(url)
    return wrapper

@count_calls
def get_pages(url: str) -> str:
    '''returns the html content of url'''
    html_content = requests.get(url)
    return html_content.text

if __name__ == '__main__':
    get_pages("http://slowwly.robertomurray.co.uk")