import redis
import requests
from functools import wraps
from typing import Callable

# Initialize Redis client
cache = redis.Redis(host='localhost', port=6379, db=0)

def cache_page(expiration: int = 10) -> Callable:
    """
    Decorator to cache the result of a function in Redis.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(url: str) -> str:
            # Increment the count for the URL
            cache.incr(f"count:{url}")
            
            # Check if the URL is cached
            cached_page = cache.get(url)
            if cached_page:
                return cached_page.decode('utf-8')

            # Fetch the page content
            result = func(url)

            # Cache the result with an expiration time
            cache.setex(url, expiration, result)
            
            return result
        return wrapper
    return decorator

@cache_page(expiration=10)
def get_page(url: str) -> str:
    """
    Fetches the HTML content of a URL.
    """
    response = requests.get(url)
    return response.text

if __name__ == "__main__":
    url = "http://slowwly.robertomurray.co.uk/delay/5000/url/http://www.google.com"

    # Fetch the page and print the result
    print(get_page(url))
    
    # Print the access count
    print(f"URL accessed {cache.get(f'count:{url}').decode('utf-8')} times")