#!/usr/bin/env python3

""" Asynchronous Comperhensions """
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ Creates a list of 10 numbers from a 10-number generator. """
    return [asyncomp async for asyncomp in async_generator()]
