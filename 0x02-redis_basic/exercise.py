#!/usr/bin/env python3
'''A module for a Cache class'''
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Callable]) -> Union[str, bytes, int, float, list, None]:
        '''Gets data from redis and converts it to fn'''
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
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
