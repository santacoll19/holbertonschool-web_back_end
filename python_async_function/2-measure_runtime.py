#!/usr/bin/env python3
"""measure the runtime"""
import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n
# importing wait_n from 1-concurrent_coroutines.py


def measure_time(n: int, max_delay: int) -> float:
    """measures the total execution time for wait_n(n, max_delay)"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    # Calculate and return the average execution time per call
    return total_time / n
