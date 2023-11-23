from typing import List

from src.edge import Edge
from src.node import Node
index = 0

class AttackTree(object):
    """
    'AT' objects representation of a complexer hole.
    """
    def __init__(self, nodes: List[Node], edges: List[Edge]):
        """
        Creates a graph.
        :param nodes: Represent the nodes
        :param edges: Represent the edges
        """
        global index
        self._nodes = nodes
        self._edges = edges
        self.index = index
        index += 1

    def __repr__(self):
        """
        A programmer-friendly representation of the attack tree.
        :return: The string to approximate the constructor arguments of the 'AT'
        """
        return 'Attack tree(Nodes={}, Edges={}, index={)'.format(self.edges, self.nodes, self.index)

    def __str__(self) -> str:
        """
        A user-friendly representation of this attack tree
        :return: A user-friendly representation of this attack tree
        """
        return '({},{}, {})'.format(str(self.index),str(self.nodes), str(self.edges))

    @property
    def nodes(self):
        return self._nodes

    @property
    def edges(self):
        return self._edges
