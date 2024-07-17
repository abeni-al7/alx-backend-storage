#!/usr/bin/env python3
'''A module for a Cache class'''
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def replay(method: Callable) -> None:
    '''Prints information about the history of method'''
    r = redis.Redis()
    m_name = method.__qualname__
    count = int(r.get(m_name))
    print(f"{m_name} was called {str(count)} times:")
    inputs = r.lrange(f'{m_name}:inputs', 0, -1)
    outputs = r.lrange(f'{m_name}:outputs', 0, -1)
    for input, output in zip(inputs, outputs):
        print(
            f'{m_name}(*{(input.decode("utf-8"))}) -> {output.decode("utf-8")}'
            )


def call_history(method: Callable) -> Callable:
    '''A decorator to store inputs and outputs of method'''
    input_key = method.__qualname__ + ":inputs"
    output_key = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args):
        '''adds the inputs and outputs to redis'''
        self._redis.rpush(input_key, str(args))
        output = method(self, *args)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    '''A decorator to count calls'''
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Increments the count for key'''
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache:
    '''A Cache class'''
    def __init__(self):
        '''Initializing method'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores data to redis and returns the random key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[
                                            str, bytes, int, float, list, None
                                                    ]:
        '''Gets data from redis and converts it to fn'''
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        '''Gets a string data from redis'''
        try:
            return self.get(key, fn=lambda d: d.decode('utf-8'))
        except Exception:
            return None

    def get_int(self, key: str) -> Union[int, None]:
        '''Gets an int data from redis'''
        try:
            return self.get(key, fn=int)
        except Exception:
            return None
