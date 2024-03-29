from abc import ABC, abstractmethod

"""Abstract class for the semi-ring"""
class SemiRing(ABC):
    def __init(self, field):
        self._field = field

    @abstractmethod
    def root_or_operator(self, array_of_numbers):
        pass

    @abstractmethod
    def root_and_operator(self, array_of_numbers):
        pass

    @abstractmethod
    def or_operator(self, array_of_numbers):
        pass

    @abstractmethod
    def and_operator(self, array_of_numbers):
        pass

    @abstractmethod
    def reverse_and(self, number):
        pass

    @property
    def field(self):
        return self._field

"""Minimal cost implemintation of the same ring"""
class MiniumCostMetricTree(SemiRing):
    def __init__(self, field):
        self._field = field

    @classmethod
    def root_or_operator(cls, array_of_numbers):
        return min(array_of_numbers)

    @classmethod
    def root_and_operator(cls, array_of_numbers):
        return sum(array_of_numbers)

    @classmethod
    def or_operator(cls, array_of_numbers):
        return min(array_of_numbers)

    @classmethod
    def and_operator(cls, array_of_numbers):
        return sum(array_of_numbers)

    @classmethod
    def reverse_and(cls, number):
        return -number
