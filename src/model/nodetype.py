from enum import Enum


class NodeType(Enum):
    """
    Enum class for all types of Nodes, might get added some versions later on.
    """
    ROOT = 0
    BAS = 1
    OR = 2
    AND = 3
