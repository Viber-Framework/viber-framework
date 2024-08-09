from abc import ABC, abstractmethod


class Filter(ABC):

    @abstractmethod
    async def __call__(self):
        pass

    def __invert__(self):
        pass

    def __await__(self):
        return self.__call__
