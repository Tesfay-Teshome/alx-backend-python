#!/usr/bin/env python3

""" Asynchronous Comperhensions """
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehesion() -> List[float]:
    a = [i async for i in async_generator()]
    return a
