#!/usr/bin/env python3
'''A module for a Cache class'''
import redis
import uuid
from typing import Union


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
