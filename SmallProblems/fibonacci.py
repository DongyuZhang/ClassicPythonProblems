from typing import Dict
from functools import lru_cache
from typing import Generator

memo: Dict[int, int] = {0: 0, 1: 1}

def fib1(n: int) -> int:
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)

def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = memo[n-1] + memo[n-2]
    return memo[n]

@lru_cache(maxsize=None)
def fib3(n: int) -> int:
    if n < 2:
        return n
    return fib3(n-1) + fib3(n-2)

def fib4(n: int) -> int:
    if n == 0:
        return 0
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last+next
    return next

def fib5(n: int) -> int:
    yield 0
    if(n > 0): yield 1
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last+next
        yield next
