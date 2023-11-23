from abc import ABC, abstractmethod


class SemiRing(ABC):
    def __init(self, field):
        self._field = field

    @abstractmethod
    def or_operator(self, left, right):
        pass

    @abstractmethod
    def and_operator(self, left, right):
        pass

    @property
    def field(self):
        return self._field
