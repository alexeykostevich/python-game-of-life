from abc import ABCMeta, abstractproperty, abstractmethod
from typing import Generic, Iterable, TypeVar, Tuple


T = TypeVar('T')
UniverseType = TypeVar('UniverseType', bound='Universe[T]')


class Universe(Generic[T]):
    """Represents the universe of 'The Game of Life'."""
    __metaclass__ = ABCMeta

    @abstractproperty
    def width(self) -> int:
        """Returns universe width."""
        pass

    @abstractproperty
    def height(self) -> int:
        """Returns universe height."""
        pass

    @abstractmethod
    def through(self) -> Tuple[int, int]:
        """Returns a new iterator that can iterate over the universe."""
        pass

    @abstractmethod
    def neighbours_of(self, x: int, y: int) -> Iterable[T]:
        """Returns a new iterator that can iterate over neighbours around the specified position."""
        pass

    @abstractmethod
    def __copy__(self) -> UniverseType:
        """Returns a shallow copy of the universe."""
        pass

    @abstractmethod
    def __getitem__(self, position: Tuple[int, int]) -> T:
        """Returns a value for the specified position using self[x, y]."""
        pass

    @abstractmethod
    def __setitem__(self, position: Tuple[int, int], value: T):
        """Sets the value for the specified position using self[x, y]."""
        pass
