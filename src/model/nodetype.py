from enum import Enum


class NodeType(Enum):
    """
    Enum class for all types of Nodes, might get added some versions later on.
    """
    ROOT_OR = 0
    ROOT_AND = 1
    BAS = 2
    OR = 3
    AND = 4
