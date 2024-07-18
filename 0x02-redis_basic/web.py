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
        page = r.get(url)
        if page:
            return page.decode('utf-8')

        key = 'count:' + url
        result = fn(url)
        r.incr(key)
        r.set(url, result, ex=10)
        r.expire(url,)
        return result
    return wrapper


@count_calls
def get_page(url: str) -> str:
    '''returns the html content of url'''
    html_content = requests.get(url)
    return html_content.text
