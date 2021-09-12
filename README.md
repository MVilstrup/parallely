# Parallely - Parallel Python made simple

[![pypi](https://img.shields.io/pypi/v/parallely.svg)](https://pypi.org/project/parallely/)
[![License](https://img.shields.io/github/license/mvilstrup/parallely)](https://github.com/mvilstrup/parallely/blob/main/LICENSE)
[![wheel](https://img.shields.io/pypi/wheel/parallely.svg)](https://pypi.org/project/parallely/)
[![python](https://img.shields.io/pypi/pyversions/parallely.svg)](https://pypi.org/project/parallely/)
[![Test Suite](https://github.com/mvilstrup/parallely/workflows/Test%20Suite/badge.svg)](https://github.com/mvilstrup/parallely/actions?query=workflow%3A%22Test+Suite%22)
[![Coverage Status](https://coveralls.io/repos/github/MVilstrup/parallely/badge.svg?branch=main)](https://coveralls.io/github/MVilstrup/parallely?branch=main)
[![docs](https://readthedocs.org/projects/parallely/badge/?version=latest)](https://parallely.readthedocs.io/en/latest/?badge=latest)


# Installation
`pip install parallely`

# Multi Threading

```python
import time
from parallely import threaded

@threaded
def thread_function(name, duration=2):
    print(f"Thread {name}: starting")
    time.sleep(duration)
    print(f"Thread {name}: finishing")


print("Synchronous")
thread_function(1, duration=2)
thread_function(2, duration=1)

print()
print("Asynchronous")
thread_function.map(name=[1, 2], duration=[2, 1])
```

# Multi Processing

```python
from time import time
from random import randint
from parallely import parallel


@parallel
def count_in_range(size, search_minimum, search_maximum):
    """Returns how many numbers lie within `maximum` and `minimum` in a random array"""
    rand_arr = [randint(0, 10) for _ in range(int(size))] 
    return sum([search_minimum <= n <= search_maximum for n in rand_arr])

size = 1e7

print("Sequential")
start_time = time()
for _ in range(3):
    result = count_in_range(size, search_minimum=1, search_maximum=2)
    print(result, round(time() - start_time, 2), "seconds")

print()

print("Parallel")
start_time = time()
result = count_in_range.map(size=[size, size, size], search_minimum=1, search_maximum=2)
print(result, round(time() - start_time, 2), "seconds")
```

# Asynchronous

```python
import asyncio
import time
from random import randint
from parallely import asynced


async def echo(delay, start_time):
    await asyncio.sleep(randint(0, delay))
    print(delay, round(time.time() - start_time, 1))

@asynced
async def main(counts):
    start_time = time.time()
    print(f"started at {time.strftime('%X')}")
    
    corr = []
    for count in range(counts):
        corr.append(echo(count, start_time))
        
    await asyncio.gather(*corr)

    print(f"finished at {time.strftime('%X')}")
    
main(10)
```