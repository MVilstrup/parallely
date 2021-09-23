from typing import Any, Callable, List


class ParalellyFunction:
    def __init__(self, func: Callable, max_workers: int):

        self._func = func
        self._max_workers = max_workers

    def map(self, *args, **kwargs) -> List[Any]:
        raise NotImplementedError("All children should implement map")

    def imap(self, *args, **kwargs) -> List[Any]:
        raise NotImplementedError("All children should implement imap")

    def acmap(self, *args, **kwargs) -> List[Any]:
        raise NotImplementedError("All children should implement acmap")

    def flat_map(self, *args, **kwargs) -> List[Any]:
        raise NotImplementedError("All children should implement flat_map")

    def iflat_map(self, *args, **kwargs) -> List[Any]:
        raise NotImplementedError("All children should implement iflat_map")

    def acflat_map(self, *args, **kwargs) -> List[Any]:
        raise NotImplementedError("All children should implement acflat_map")

    def then(self, callable):
        raise NotImplementedError("All children should implement then")

    def _execute_once(self, *args, **kwargs) -> Any:
        raise NotImplementedError()

    def __call__(self, *args, **kwargs) -> Any:
        return self._execute_once(*args, **kwargs)
