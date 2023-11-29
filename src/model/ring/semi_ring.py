from abc import ABC, abstractmethod


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

    @property
    def field(self):
        return self._field


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



class MiniumCostMetricGraph(SemiRing):
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
