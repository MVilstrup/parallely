from concurrent.futures import ThreadPoolExecutor
from functools import partial
from multiprocessing import cpu_count
from typing import Any, Callable, List, Optional

from parallely.base import ParalellyFunction
from parallely.utils import prepare_arguments


class ThreadedFunction(ParalellyFunction):
    def _execute_once(self, *args, **kwargs) -> Any:
        return self._func(*args, **kwargs)

    def map(self, *args, **kwargs) -> List[Any]:
        args, kwargs = prepare_arguments(args, kwargs)
        pool_size = min(self._max_workers, len(args))

        with ThreadPoolExecutor(pool_size) as pool:
            futures = [pool.submit(self._execute_once, *arg, **kwarg) for arg, kwarg in zip(args, kwargs)]

        return [future.result() for future in futures]


def threaded(func: Callable = None, max_workers: Optional[int] = None) -> ThreadedFunction:
    """

    :param func:
    :param max_workers:
    :return:
    """

    max_workers = max_workers if max_workers is not None else cpu_count() * 10

    if func is None:
        return partial(threaded, max_workers=max_workers)

    return ThreadedFunction(func, max_workers)
