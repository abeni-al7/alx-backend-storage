#!/usr/bin/env python3
'''A module for a Cache class'''
import redis
import uuid
from typing import Union, Callable


class Cache:
    '''A Cache class'''
    def __init__(self):
        '''Initializing method'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Stores data to redis and returns the random key'''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable) -> any:
        '''Gets data from redis and converts it to fn'''
        try:
            if fn != None:
                return fn(self._redis.get(key))
            return self._redis.get(key)
        except Exception:
            return None

    def get_str(self, key: str) -> Union[str, None]:
        '''Gets a string data from redis'''
        try:
            return str(self.get(key))
        except Exception:
            return None

    def get_int(self, key: str) -> Union[int, None]:
        '''Gets an int data from redis'''
        try:
            return int(self.get(key))
        except Exception:
            return None
