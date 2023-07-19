#!/usr/bin/env python3
"""a cache class that has Redis client as private variale
Has a store method that takes data and returns a string
The method generates a random key using uuid and stores input
data using random key and returns the key"""


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """decorator for counting no of calls a function is called"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper for decorator"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """define input and output list keys"""
    input_key = f"{method.__qualname__}:inputs"
    output_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """append input args to input list using rpush"""
        self._redis.rpush(input_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(output_key, output)
        return output
    return wrapper


class Cache:
    """class that stores an instance of redis client
    and stores data"""
    def __init__(self):
        """stores redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """generate random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """retrive data from redis using a given key"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """returns data as string using get method"""
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """return data as integer"""
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0
        return val

    def replay(method: Callable):
        """get instance od cache from mthod's first args"""
        inst = method.__self__
        qualname = method.__qualname__
        count = inst._redis.get(qualname).decode("utf-8")
        print(f"{qualname} was called {count} times:")
        input_key = f"{qualname}:inputs"
        output_key = f"{qualname}:outputs"
        """get all elements from both lists using lrange"""
        inputs = inst._redis.lrange(input_key, 0, -1)
        outputs = inst._redis.lrange(output_key, 0, -1)
        for i, (input_, output) in enumerate(zip(inputs, outputs)):
            input_ = input_.decode("utf-8")
            output = output.decode("utf-8")
            print(f"{i + 1}. {qualname}(*{input_}) -> {output}")
