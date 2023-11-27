from abc import ABC, abstractmethod


class SemiRing(ABC):
    def __init(self, field):
        self._field = field

    @abstractmethod
    def or_operator(self, array_of_numbers):
        pass

    @abstractmethod
    def and_operator(self, array_of_numbers):
        pass

    @property
    def field(self):
        return self._field


class MiniumCostMetric(SemiRing):
    def __init__(self, field):
        self._field = field

    @classmethod
    def or_operator(self, array_of_numbers):
        return min(array_of_numbers)

    @classmethod
    def and_operator(self, array_of_numbers):
        return sum(array_of_numbers)
