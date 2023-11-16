from typing import List

from src.edge import Edge
from src.node import Node


class AttackTree(object):
    def __init__(self, nodes: List[Node], edges: List[Edge]):
        self._nodes = nodes
        self._edges = edges

    def __repr__(self):
        """
        A programmer-friendly representation of the attack tree.
        :return: The string to approximate the constructor arguments of the 'AT'
        """
        return 'Attack tree(Nodes={}, Edges={})'.format(self.edges, self.nodes)

    def __str__(self) -> str:
        """
        A user-friendly representation of this attack tree
        :return: A user-friendly representation of this attack tree
        """
        return '({}, {})'.format(str(self.nodes), str(self.edges))

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges
