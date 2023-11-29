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
    def root_or_operator(cls, mapping):
        return min(mapping)

    @classmethod
    def root_and_operator(cls, mapping):
        # Glue all node result together
        mapping_attribute = {}
        for result in mapping:
            mapping_attribute = mapping_attribute | result[0][1]
        # Reduce result.
        mapping_value = []
        added_nodes = []
        value = 0
        # Adding for the min/max
        for result in mapping:
            value += result[0][0][0]
            for node in result[0][0][1]:
                if node not in added_nodes:
                    added_nodes += [node]
                else:
                    # Node is already added, so subtract value.
                    for map in mapping_attribute:
                        if map[1] == node:
                            value -= map[0]
        mapping_value = [value, added_nodes]
        return [mapping_value, mapping_attribute]

    @classmethod
    def or_operator(cls, mapping):
        # Glue all node result together
        mapping_attribute = {}
        for result in mapping:
            mapping_attribute = mapping_attribute | result[0][1]
        mapping_value = []
        # We need to check for duplicated and reduce those
        combination_added = []
        for result in mapping:
            if result[0][0][1] not in combination_added:
                combination_added += [result[0][0][1]]
                mapping_value += [result[0][0]]
            else:
                # Check what value is already added.
                for m_value in mapping_value:
                    m_value
        return [[mapping_value, mapping_attribute]]

    @classmethod
    def and_operator(cls, mapping):
        # Glue all node result together
        mapping_attribute = {}
        for result in mapping:
            mapping_attribute = mapping_attribute | result[0][1]
        # Reduce result
        added_nodes = []
        value = 0
        # Adding for the min/max
        for result in mapping:
            value += result[0][0][0]
            for node in result[0][0][1]:
                if node not in added_nodes:
                    added_nodes += [node]
                else:
                    # Node is already added, so subtract value.
                    value -= mapping_attribute[node]
        mapping_value = [value, added_nodes]
        return [mapping_value, mapping_attribute]
