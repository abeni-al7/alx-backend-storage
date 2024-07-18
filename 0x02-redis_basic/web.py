#!/usr/bin/env python3
'''A module for fetching the html content of a page and caching
the result in redis'''
import requests
import redis
from functools import wraps
from typing import Callable

# Initialize Redis connection
redis_client = redis.Redis()


def cache_page(func: Callable) -> Callable:
    '''A decorator for caching a page'''
    @wraps(func)
    def wrapper(url: str) -> str:
        '''Wrapper that caches html content'''
        # Generate cache and count keys
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"

        # Increment the access count
        redis_client.incr(count_key)

        # Check if the URL content is cached
        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # Fetch the content using the original function
        content = func(url)

        # Cache the content with an expiration time of 10 seconds
        redis_client.setex(cache_key, 10, content)

        return content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    '''Get a page from a url'''
    response = requests.get(url)
    return response.text
